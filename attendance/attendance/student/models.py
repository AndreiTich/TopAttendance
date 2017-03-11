from django.db import models

class Attendance(models.Model):
    student_id = models.CharField(max_length=8)
    code = models.CharField(max_length=4)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)