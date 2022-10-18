# docker-compose run api python manage.py makemigrations
# docker-compose run api python manage.py migrate

from django.db import models

class Placeholder(models.Model):
    placeholder = models.CharField(max_length=100)
