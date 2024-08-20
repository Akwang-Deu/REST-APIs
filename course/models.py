from django.db import models

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=20)
    course_id = models.PositiveSmallIntegerField()
    topics = models.PositiveSmallIntegerField()
    teacher_in_charge = models.CharField(max_length=20)
    duration = models.TimeField()
    Students_enrolled = models.PositiveSmallIntegerField()
    department = models.TimeField()
    start_date = models.CharField(max_length=20)
    end_date = models.CharField(max_length=20)
    assessment_method = models.CharField(max_length=20)
    

    def __str__(self):
        return f"{self.title}"


