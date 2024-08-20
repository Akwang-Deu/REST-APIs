from django.db import models

# Create your models here.
class Courses(models.Model):
    course = models.CharField(max_length=80)



class Student(models.Model):
    courses = models.ManyToManyField(Courses)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    country = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    code = models.PositiveSmallIntegerField()
    age = models.PositiveSmallIntegerField(default =0)
    gender = models.CharField(max_length=10 ,default=0)
    contact = models.CharField(max_length=20 ,default=0)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

