# Generated by Django 4.0.6 on 2022-08-06 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_alter_school_graduation_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='social',
            name='icon',
        ),
    ]
