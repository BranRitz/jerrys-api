from rest_framework import generics
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from survey_api.forms import SignUpForm


class WIP(generics.ListAPIView):
    """
    WIP page
    """
    # @login_required
    def get(self, request, *args, **kwargs):
        return render(request, 'survey_api/wip.html')

@login_required
def index(request):
    return render(request, 'survey_api/index.html')

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
    return render(request, 'survey_api/signup.html', {'form': form})
