from django.db import models

# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    country = models.CharField()
    course = models.CharField()
    teacher_id = models.PositiveSmallIntegerField()
    hire_date = models.DateField()
    contact = models.CharField()
    gender = models.CharField()
    specialization = models.CharField()

   

def __str__(self):
        return f"{self.first_name} {self.last_name}"

