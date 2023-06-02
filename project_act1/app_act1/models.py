from django.db import models


class StudentInfo(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)       

    class Meta:
        managed = True
        db_table = 'student_info'