# docker-compose run api python manage.py makemigrations
# docker-compose run api python manage.py migrate

from django.contrib.postgres.fields import JSONField
from django.db import models


class UserHistory(models.Model):
    user = models.CharField(max_length=100)
    history = JSONField(default=dict)


