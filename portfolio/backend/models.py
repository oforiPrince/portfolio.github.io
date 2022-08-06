from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Career(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title


class School(models.Model):
    name = models.CharField(max_length=100)
    short_information = models.TextField(max_length=250, null=True, blank=True)
    location = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    entry_year = models.IntegerField()
    graduation_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Social(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(
        upload_to='uploads/images/service_icons/', blank=True)
    service_description = models.TextField(max_length=100)

    def get_icon_url(self):
        if self.icon:
            return self.icon.url
        else:
            pass

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(
        upload_to='uploads/images/testimonial_pics/', blank=True)
    testimonial = models.TextField(max_length=500)
    company_name = models.CharField(max_length=100)

    def get_photo_url(self):
        return self.photo.url

    def __str__(self):
        return self.name


class Knowledge(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(validators=[
        MaxValueValidator(100),
        MinValueValidator(1)
    ], null=True, blank=True)

    def __str__(self):
        return self.name


class AcquiredSkill(models.Model):
    name = models.CharField(max_length=100)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name


class FriendlyFrameWork(models.Model):
    name = models.CharField(max_length=25)
    icon = models.ImageField(upload_to='uploads/images/friendly_frameworks/')
    years_of_experience = models.IntegerField(default=1)

    def get_icon_url(self):
        return self.icon.url

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(
        upload_to='uploads/images/certificate_pics/', blank=True)
    year = models.IntegerField()

    def __str__(self):
        return self.name


class ProjectType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, null=True, blank=True)
    number_of_projects = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    project_type = models.OneToOneField(
        ProjectType, on_delete=models.PROTECT, null=True, blank=True)
    description = models.TextField(max_length=500)
    applied_knowledge = models.ManyToManyField(Knowledge)
    hosted_link = models.CharField(max_length=100, null=True, blank=True)
    year = models.IntegerField()
    main_image = models.ImageField(
        upload_to='uploads/images/project_pics/', blank=True, null=True)

    class Meta:
        db_table = 'projects'
        verbose_name = 'project'
        verbose_name_plural = 'projects'

    def get_main_image_url(self):
        return self.main_image.url

    def __str__(self):
        return self.name


class Resume(models.Model):
    domain = models.CharField(max_length=100)
    projects = models.ManyToManyField(Project)
    certificate = models.ManyToManyField(
        Certificate)
    knowledge = models.ManyToManyField(Knowledge)
    acquired_skill = models.ManyToManyField(
        AcquiredSkill)

    def __str__(self):
        return self.domain


class SeekHelp(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=30)
    message = models.TextField(max_length=100)

    def __str__(self):
        return self.name


class SpokenLanguage(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
