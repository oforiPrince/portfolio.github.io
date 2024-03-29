from turtle import title
from django.db import models
from accounts.models import User
from ckeditor.fields import RichTextField


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Blog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    main_image = models.ImageField(upload_to='blog/main_image/')
    title = models.CharField(max_length=255, unique=True)
    category = models.OneToOneField(
        Category, on_delete=models.PROTECT, null=True, blank=True)
    body = RichTextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    def get_blog_image_url(self):
        return self.main_image.url

    class Meta:
        db_table = 'blogs'
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
