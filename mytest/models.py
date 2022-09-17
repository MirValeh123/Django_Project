from distutils.command.upload import upload
from pickle import TRUE
from unicodedata import category
from django.db import models

# from mytest.models import User
# Create your models here.


class AddWork(models.Model):
    author = models.ForeignKey(
        'custom_user.MyUser', on_delete=models.CASCADE, verbose_name='author')
    title = models.CharField(max_length=50, verbose_name='title')
    content = models.TextField(verbose_name='content')
    created_date = models.DateField(auto_now=True, verbose_name='Date')
    image = models.FileField(upload_to='#pic', verbose_name='image')
    client = models.CharField(max_length=20, verbose_name='client', blank=True)
    category = models.CharField(
        max_length=30, verbose_name='category', blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(
        AddWork, on_delete=models.CASCADE, verbose_name='article', related_name='comments')
    comment_author = models.CharField(max_length=50, verbose_name='author')
    comment_content = models.CharField(max_length=200, verbose_name='content')
    comment_date = models.DateTimeField(
        auto_now_add=True, verbose_name='date', null=True, blank=True)

    def __str__(self):
        return self.comment_content
