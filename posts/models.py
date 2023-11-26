from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.category


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.ManyToManyField(Category)
    image = models.ImageField(
        upload_to='images/', default='../default_post_etnxul', blank=True
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.id} {self.title}'