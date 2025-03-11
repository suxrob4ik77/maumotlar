
from django.db import models

from django.contrib.auth.models import User
class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=50, verbose_name='news')
    context = models.TextField(blank=True)
    created_ed = models.DateTimeField(auto_now_add=True)
    updated_ed = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="get_news")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_bool = models.BooleanField(default=True)
    views=models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "NEW"
        verbose_name_plural = "NEWS"
        ordering = ['-created_ed']


class BaseUser(models.Model):
    pass
