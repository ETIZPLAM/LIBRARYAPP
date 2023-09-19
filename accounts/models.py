from django.db import models

class accountsclass(models.Model):
    Fname=models.CharField(max_length=30)
    Lname=models.CharField(max_length=30)
    booksname=models.CharField(max_length=30)
    age=models.IntegerField()
    created_at=models.DateTimeField(blank=True,null=True)
    updated_at=models.DateTimeField(blank=True,null=True)
