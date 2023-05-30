from django.db import models


class StudentInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)       

    class Meta:
        managed = False
        db_table = 'student_info'