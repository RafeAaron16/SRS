from django.db import models

# Create your models here.
class Student(models.Model):
        Fname = models.CharField(max_length=20)
        Lname = models.CharField(max_length=20)
        usr = models.CharField(max_length=16, unique=True)
        email = models.CharField(max_length=40, unique=True)
        password = models.CharField(max_length=20)

        def __str__(self):
                return self.email
