# Generated by Django 4.0.6 on 2022-07-10 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_school_short_information_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='main_image',
            field=models.ImageField(upload_to='uploads/images/project_pics/'),
        ),
        migrations.DeleteModel(
            name='ProjectImage',
        ),
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='backend.projecttype'),
        ),
    ]
