# Imports

# 3rd party
from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Class for Follower Model
    'Owner' follows other users
    'Followed' is being followed by other users
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following'
    )
    followed = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followed'
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['owner', 'followed']
        ordering = ['-created_on']
    
    def __str__(self):
        return f'{self.owner} {self.followed}'