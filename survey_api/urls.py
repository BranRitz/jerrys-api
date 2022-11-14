from django.urls import path
# from django.contrib import admin
from django.conf.urls import url
from survey_api import views
from rest_framework.urlpatterns import format_suffix_patterns
# import forms_builder.forms.urls

urlpatterns = [
    path('', views.index),
    url(r'^v1/professor/surveys', views.professor_surveys_base),
    url(r'^v1/professor/questions', views.professor_view_questions),
    url(r'^v1/professor/data', views.dummy_data),
    url(r'^v1/professor', views.professor_index),
    url(r'^v1/student', views.student_index),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^sort/$', views.sort),
    url(r'^status', views.status),
    url(r'^close-status', views.close_status),
    url(r'^open-status', views.open_status),

    # url(r'^forms/', include(forms_builder.forms.urls)),

    # url(r'^v1/professor/surveys', views.WIP.as_view()),
    # url(r'^v1/prof/courses', views.WIP.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
