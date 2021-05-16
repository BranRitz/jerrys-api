# Generated by Django 3.0.14 on 2021-05-16 15:27

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('history', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
            ],
        ),
    ]
