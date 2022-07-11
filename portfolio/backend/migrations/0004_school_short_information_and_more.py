# Generated by Django 4.0.6 on 2022-07-09 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_friendlyframework'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='short_information',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='service_description',
            field=models.TextField(max_length=100),
        ),
    ]