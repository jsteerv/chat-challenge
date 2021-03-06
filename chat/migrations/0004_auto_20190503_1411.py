# Generated by Django 2.2 on 2019-05-03 14:11

from django.db import migrations
from django.contrib.auth.models import User
from chat.models import Room


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_room_users'),
    ]

    def insert_data(apps, schema_editor):
        user = User.objects.create_superuser('admin', 'myuser@mydomain.com', 'jobsitychallenge')
        user.save()
        user = User.objects.create_user('user1', 'myuser@mydomain.com', 'chatpass1')
        user.save()
        user = User.objects.create_user('user2', 'myuser@mydomain.com', 'chatpass2')
        user.save()
        room = Room.objects.create(name='Room 1')
        room.save()
        room = Room.objects.create(name='Room 2')
        room.save()
        room = Room.objects.create(name='Room 3')
        room.save()

    operations = [
        migrations.RunPython(insert_data),
    ]
