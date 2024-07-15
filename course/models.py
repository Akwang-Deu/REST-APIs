from django.db import models

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=20)
    course_code = models.PositiveSmallIntegerField()
    topics = models.PositiveSmallIntegerField()
    teacher_in_charge = models.CharField()
    duration = models.TimeField()
    Students_enrolled = models.PositiveSmallIntegerField()
    department = models.TimeField()
    start_date = models.CharField()
    end_date = models.CharField()
    assessment_method = models.CharField()
    

    def __str__(self):
        return f"{self.title}"


