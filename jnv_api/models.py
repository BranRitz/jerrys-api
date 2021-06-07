# docker-compose run api python manage.py makemigrations
# docker-compose run api python manage.py migrate

from django.contrib.postgres.fields import JSONField, ArrayField
from django.db import models


class UserHistory(models.Model):
    user = models.CharField(max_length=100)
    history = JSONField(default=dict)


class WordLists(models.Model):
    category = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    word_list = ArrayField(models.CharField(max_length=100))