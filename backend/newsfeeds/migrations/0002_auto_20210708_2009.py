# Generated by Django 3.2.4 on 2021-07-08 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeeds', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='detail',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='overview',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]