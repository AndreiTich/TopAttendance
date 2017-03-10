from django.db import models

class Attendance(models.Model):
    student_id = models.CharField(max_length=8)
    code = models.CharField(max_length=4)