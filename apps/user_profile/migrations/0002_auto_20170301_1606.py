# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='avatar',
            field=models.ImageField(default='login_register/avatar/default/default.jpg', upload_to='login_register/avatar/'),
        ),
    ]
