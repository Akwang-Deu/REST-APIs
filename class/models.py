from django.db import models

# Create your models here.

class Class(models.Model):
    class_name = models.CharField(max_length=20)
    class_capacity = models.PositiveSmallIntegerField()
    teacher_in_charge = models.CharField()
    no_of_groups = models.PositiveSmallIntegerField()
    description = models.PositiveSmallIntegerField()
    course = models.PositiveSmallIntegerField()
    schedule = models.CharField()
    artwork = models.CharField()
    class_representative = models.CharField()
    room_number = models.PositiveSmallIntegerField()
    

    def __str__(self):
        return f"{self.class_name}"


