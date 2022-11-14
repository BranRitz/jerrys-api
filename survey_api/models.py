# docker-compose run api python manage.py makemigrations
# docker-compose run api python manage.py migrate

from django.contrib.postgres.fields import JSONField, ArrayField

from django.db import models

# class Placeholder(models.Model):
#     placeholder = models.CharField(max_length=100)

class AccountTypes(models.Model):
    username = models.CharField(max_length=100)
    account_type = models.CharField(max_length=100)

class Surveys(models.Model):
    owner = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    questions = ArrayField(models.CharField(max_length=1000))
    course = models.ForeignKey("Courses", on_delete=models.CASCADE)

class Courses(models.Model):
    professor = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    students = ArrayField(models.CharField(max_length=100))

class SurveyAnswers(models.Model):
    student_username = models.CharField(max_length=100)
    survey = models.ForeignKey("Surveys", on_delete=models.CASCADE)
    answers = JSONField(default=dict)

    # class SurveyAnswers(models.Model):
#     professor = models.CharField(max_length=100)
#     student = models.CharField(max_length=100)
#     survey_name = models.CharField(max_length=100)
#
#
#
#
#
#
#
# # docker-compose run api python manage.py makemigrations
# # docker-compose run api python manage.py migrate
#
#
#
# from django.contrib.postgres.fields import JSONField, ArrayField
# from django.db import models
#
#
# class UserHistory(models.Model):
#     user = models.CharField(max_length=100)
#     history = JSONField(default=dict)
#
#
# class WordLists(models.Model):
#     category = models.CharField(max_length=100)
#     level = models.CharField(max_length=100)
#     word_list = ArrayField(models.CharField(max_length=100))