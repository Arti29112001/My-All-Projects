# Generated by Django 4.1.3 on 2022-12-09 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0002_userinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='username',
            new_name='uname',
        ),
    ]
