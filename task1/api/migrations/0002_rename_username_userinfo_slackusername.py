# Generated by Django 4.1.1 on 2022-10-29 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='username',
            new_name='slackUsername',
        ),
    ]
