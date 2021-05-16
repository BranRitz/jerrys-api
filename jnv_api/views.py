from rest_framework import generics
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from jnv_api.serializers import UserHistorySerializer
from jnv_api.models import UserHistory
from jnv_api.forms import SignUpForm, AttemptForm


class AdminUserHistory(generics.ListAPIView):
    """
    View all user history objects, only for admin.
    """
    queryset = UserHistory.objects.all()
    serializer_class = UserHistorySerializer


class DbUserHistory(APIView):
    def get(self, request, *args, **kwargs):
        """
        Take the username from request and return the user history JSON.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        pass

    def post(self, request, *args, **kwargs):
        """
        Create a new user history row. Only happens once for a new user, then we just update the history.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        pass

    def put(self, request, *args, **kwargs):
        """
        Update a history JSON for a user.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        pass


@login_required
def index(request):
    return render(request, 'jnv_api/index.html')

@login_required
def word_attempt_view(request):
    form = AttemptForm()
    if request.method == "POST":
        form = AttemptForm(request.POST)
        if form.is_valid():
            print("Word: "+form.cleaned_data['word'])
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
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'jnv_api/signup.html', {'form': form})
