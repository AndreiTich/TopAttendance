from django.db import models

class Attendance(models.Model):
    class_code = models.CharField(max_length=4)
