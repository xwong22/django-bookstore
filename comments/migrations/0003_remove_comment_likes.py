# Generated by Django 4.1.3 on 2022-12-12 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_remove_comment_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='likes',
        ),
    ]
