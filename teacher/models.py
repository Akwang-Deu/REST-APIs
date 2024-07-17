from django.db import models

# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    country = models.CharField(max_length=20)
    course = models.CharField(max_length=20)
    teacher_id = models.PositiveSmallIntegerField()
    hire_date = models.DateField()
    contact = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    specialization = models.CharField(max_length=20)

   

def __str__(self):
        return f"{self.first_name} {self.last_name}"

