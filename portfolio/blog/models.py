from turtle import title
from django.db import models
from accounts.models import User
from ckeditor.fields import RichTextField


class Tag(models.Model):
    name = models.CharField(max_length=30)


class Blog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    main_image = models.ImageField(upload_to='blog/main_image/')
    title = models.CharField(max_length=255, unique=True)
    body = RichTextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blogs'
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
