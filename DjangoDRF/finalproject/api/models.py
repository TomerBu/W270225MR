from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Profile of {self.user.username}'

    def __repr__(self):
        return f'UserProfile(user={self.user.username}, bio={self.bio}, birth_date={self.birth_date})'


class Tag(models.Model):
    name = models.CharField(unique=True, max_length=32)

    def __str__(self):
        return f'{self.name}'
