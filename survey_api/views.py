from rest_framework import generics
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from survey_api.models import AccountTypes, Surveys, Courses, SurveyAnswers
import json
from django.http import JsonResponse


from survey_api.forms import SignUpForm


class WIP(generics.ListAPIView):
    """
    WIP page
    """
    # @login_required
    def get(self, request, *args, **kwargs):
        return render(request, 'survey_api/wip.html')

def index(request):
    return render(request, 'survey_api/base.html')

def sort(request):
    user_info = AccountTypes.objects.filter(username=request.user).values()
    account_type = user_info[0]["account_type"]
    return redirect(f"/v1/{account_type}")


@login_required
def professor_index(request):
    return render(request, 'survey_api/prof_index.html')

@login_required
def student_index(request):
    return render(request, 'survey_api/student_index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            account_type = form.cleaned_data.get('account_type')
            AccountTypes.objects.create(username=username, account_type=account_type)

            return redirect(f"/v1/{account_type}")
    else:
        form = SignUpForm()
    return render(request, 'survey_api/signup.html', {'form': form})

@login_required
def professor_courses_base(request):
    # get all courses
    # display in form
    return render(request, 'survey_api/professor_index.html')

@login_required
def professor_surveys_base(request):
    username = request.user.username
    data = Surveys.objects.filter(owner=username).values()
    for d in data:
        print(d)
        course_id = d["course_id"]
        course = Courses.objects.filter(id=course_id).values('course_name')
        d["course"] = list(course)[0]["course_name"]

    return render(request, 'survey_api/prof_surveys.html', {"data": data})

@login_required
def professor_view_questions(request):
    sid = request.GET.get('sid')
    survey = Surveys.objects.filter(id=sid).values('questions')
    survey_qs = list(survey)[0]["questions"]
    num = 1
    q_list = []
    for q in survey_qs:
        add_this = {"number": num, "question": q}
        q_list.append(add_this)
        num = num + 1
    return render(request, 'survey_api/prof_view_qs.html', {"questions": q_list})

def status(request):
    sid = request.GET.get('sid')
    current_status = list(Surveys.objects.filter(id=sid).values('status'))[0]["status"]
    if current_status == "open":
        return render(request, 'survey_api/close_status.html', {"id": sid})
    else:
        return render(request, 'survey_api/open_status.html', {"id": sid})

def close_status(request):
    sid = request.GET.get('sid')
    Surveys.objects.filter(id=sid).values('status').update(status="closed")

    return professor_surveys_base(request)

def open_status(request):
    sid = request.GET.get('sid')
    Surveys.objects.filter(id=sid).values('status').update(status="open")

    return professor_surveys_base(request)

def dummy_data(request):
    data = {
    "professor": "bkuritz",
    "survey_data": {
        "example_survey_1": {
            "status": "open",
            "example_student_1": {
              "How many days do you study": 3,
              "What is your current grade": 82
              },
             "example_student_2": {
               "How many days do you study": 7,
               "What is your current grade": 98
              },
        },
           "example_survey_2": {
              "status": "closed",
              "example_student_1": {
                "How many dogs do you have": 3,
                "How many cats do you have": 4,
                },
            "example_student_3": {
                "How many dogs do you have": 0,
                "How many cats do you have": 0,
            },
           "example_survey_3": {
               "status": "closed",
               "example_student_1": {
                   "How many dogs do you have": 3,
                   "How many cats do you have": 4,
               },
               "example_student_4": {
                   "How many dogs do you have": 1,
                   "How many cats do you have": 1,
               },
               "example_student_5": {
                   "How many dogs do you have": 1,
                   "How many cats do you have": 2,
               },
           },

           "example_survey_4": {
               "status": "closed",
               "example_student_4": {
                   "How many dogs do you have": 3,
                   "How many cats do you have": 3,
               },
               "example_student_5": {
                   "How many dogs do you have": 2,
                   "How many cats do you have": 0,
               },
               "example_student_6": {
                   "How many dogs do you have": 1,
                   "How many cats do you have": 0,
               },
               }
           }
        }
    }

    # data_json = json.dump(data)
    return JsonResponse(data, content_type='application/json')
    # data = json.dumps(data)
    # return data.json()



@login_required
def professor_surveys_create(request):
    # get all surveys
    # display in form
    return render(request, 'survey_api/student_index.html')