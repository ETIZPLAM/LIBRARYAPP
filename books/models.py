from django.db import models

class booksclass(models.Model):
    name=models.CharField(max_length=30)
    genre=models.CharField(max_length=30)
    Condition=models.CharField(max_length=30)
