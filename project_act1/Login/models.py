from django.db import models
from app1.models import StudentInfo

class SomeModel(models.Model):
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    # 다른 필드들 추가...

    class Meta:
        managed = True
        # 테이블 이름 등 필요한 설정 추가...
