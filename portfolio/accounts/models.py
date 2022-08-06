from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import AccountManager
from backend.models import Career,SpokenLanguage,Language


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    fullname = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    spoken_languages = models.ManyToManyField(SpokenLanguage)
    programming_languages = models.ManyToManyField(Language)
    nationality = models.CharField(max_length=20,default='Ghana')
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=10)
    photo = models.ImageField(
        upload_to='uploads/profile_pics/', blank=True)
    location = models.CharField(max_length=100, blank=True)
    careers = models.ManyToManyField(Career)
    career_summary = models.TextField(max_length=500)
    cv = models.FileField(upload_to='uploads/cv/', blank=True)

    # Django stuff for authentication
    USERNAME_FIELD = "username"
    objects = AccountManager()
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    def get_cv_url(self):
        return self.cv.url

    def get_photo_url(self):
        if self.photo:
            return self.photo.url
        else:
            return '/static/frontend/images/personal/1.png'

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
