from django.urls import path
# from django.contrib import admin
from django.conf.urls import url
from survey_api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^v1/prof/surveys', views.WIP.as_view()),
    url(r'^v1/prof/courses', views.WIP.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
