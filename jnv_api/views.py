import operator
import os
import random
import statistics
from rest_framework import generics
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from jnv_api.serializers import UserHistorySerializer
from jnv_api.models import UserHistory, WordLists
from jnv_api.forms import SignUpForm, AttemptForm, ChooseWordsForm

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/jnvapi-017ea3365be3.json"
import speech_recognition as sr


class AdminUserHistory(generics.ListAPIView):
    """
    View all user history objects, only for admin.
    """
    queryset = UserHistory.objects.all()
    serializer_class = UserHistorySerializer


# def choose_words(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         form = ChooseWordsForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')
#
#     else:
#         form = ChooseWordsForm()
#
#     return render(request, 'name.html', {'form': form})


class DbUserHistory(APIView):
    def get(self, request, *args, **kwargs):
        """
        Take the username from request and return the user history JSON.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if request.user.is_authenticated:
            username = request.user.username
        else:
            return redirect('/')

        queryset = UserHistory.objects.filter(user=username).values('history')
        history = {}
        for h in queryset:
            history = h["history"]
        if len(history) == 0:
            return render(request, 'jnv_api/no_history.html', {"user": username})
        else:
            history_list = []
            for k,v in history.items():
                print("K", k)
                print("V", v)
                if v['hit'] == 0:
                    avg = "---"
                else:
                    avg = round((statistics.mean(v['hit_scores']) * 100), 2)
                    avg = str(avg) + '%'
                single_word = (k, v['hit'], v['miss'], avg)
                history_list.append(single_word)
            history_list = sorted(history_list, key=operator.itemgetter(1))
            history_list.reverse()
            return render(request, 'jnv_api/history.html', {"user": username, "history": history_list})

@csrf_exempt
def process_word(request):
    """
    Take the username from request and return the user history JSON.
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    audio_file = request.FILES.get('recorded_audio')
    intended_word = request.POST.get('intended_word')
    print("hello")
    r = sr.Recognizer()
    with sr.WavFile(audio_file) as source:  # use "test.wav" as the audio source
        audio = r.record(source)  # extract audio data from the file
    try:
        user_hist = UserHistory.objects.filter(user=request.user).values()
        history_dict = dict()
        for i in user_hist:
            history_dict = i["history"]
    except Exception as e:
        print("Issue getting user historu")
        return
    try:
        rec_list = r.recognize_google(audio, show_all=True)  # generate a list of possible transcriptions
        print(rec_list)
        for prediction in rec_list['alternative']:
            curr_word = prediction['transcript'].lower()
            if curr_word == intended_word.lower():
                score = round(prediction['confidence'] * 100, 2)
                score = str(score) + '%'
                print(f"HIT! Word: {prediction['transcript']}, Score: {score}")
                if curr_word not in history_dict:
                    add_dict = {curr_word: {"hit": 1, "miss": 0, "hit_scores": [prediction['confidence']]}}
                    history_dict.update(add_dict)
                else:
                    curr_dict = history_dict[curr_word]
                    curr_dict["hit"] = curr_dict["hit"] + 1
                    curr_dict["hit_scores"].append(prediction['confidence'])
                UserHistory.objects.filter(user=request.user).update(history=history_dict)
                return JsonResponse({'success': True, 'score': score})
            else:
                print("MISS")
                if intended_word.lower() not in history_dict:
                    add_dict = {intended_word.lower(): {"hit": 0, "miss": 1, "hit_scores": []}}
                    history_dict.update(add_dict)
                else:
                    curr_dict = history_dict[intended_word.lower()]
                    curr_dict["miss"] = curr_dict["miss"] + 1
                UserHistory.objects.filter(user=request.user).update(history=history_dict)
                return JsonResponse({'success': False})
    except LookupError:  # speech is unintelligible
        print("Could not understand audio")
        return render(request, 'jnv_api/missedword.html')


def missed_attempt(request):
    return render(request, 'jnv_api/missedword.html')


def hit_attempt(request):
    score = request.GET.get('score', '93.78%')
    return render(request, 'jnv_api/hitword.html', {'score': str(score)})


@login_required
def index(request):
    return render(request, 'jnv_api/index.html')


@login_required
def word_attempt_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = ChooseWordsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            category = form.cleaned_data['category']
            level = form.cleaned_data['level']
            words = WordLists.objects.filter(category=category, level=level).values()
            word_list = []
            for w in words:
                word_list = w["word_list"]
            end = len(word_list) - 1
            num = random.randint(0, end)
            chosen_word = word_list[num]
            return render(request, 'jnv_api/record.html', {'word': chosen_word, 'words': word_list})
    form = ChooseWordsForm()
    return render(request, 'jnv_api/form_page.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            UserHistory.objects.create(user=username)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'jnv_api/signup.html', {'form': form})

