# Generated by Django 4.0.6 on 2022-07-09 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_spokenlanguage'),
        ('accounts', '0002_user_dob_user_nationality_user_spoken_languages'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='programming_languages',
            field=models.ManyToManyField(to='backend.language'),
        ),
    ]
