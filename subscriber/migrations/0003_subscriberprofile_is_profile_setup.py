# Generated by Django 3.1 on 2020-08-29 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriber', '0002_auto_20200829_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriberprofile',
            name='is_profile_setup',
            field=models.BooleanField(default=False),
        ),
    ]
