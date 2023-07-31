from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    class_name = models.IntegerField()
    contact = models.CharField(max_length=15)