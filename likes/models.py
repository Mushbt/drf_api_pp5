from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['owner', 'post']
        ordering = ['created_on']
    
    def __str__(self):
        return f'{self.owner} {self.post}'