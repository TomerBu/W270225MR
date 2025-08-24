from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    

class Quote(models.Model):
    # props:
    author = models.CharField(max_length=60)
    quote = models.TextField()
    year = models.IntegerField()

    # admin timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)