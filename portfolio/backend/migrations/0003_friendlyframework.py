# Generated by Django 4.0.6 on 2022-07-09 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_spokenlanguage'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendlyFrameWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('icon', models.ImageField(upload_to='uploads/images/friendly_frameworks/')),
                ('years_of_experience', models.IntegerField(default=1)),
            ],
        ),
    ]