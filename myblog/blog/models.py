from django.db import models

# Django에서 model은 class 개념, models의 Model을 상속받는다!!!!!

class Post(models.Model):
    title = models.CharField(max_length=50, null=False) # 짧은 문자열 필드
    content = models.TextField() # 긴 문자열 필드
    image = models.ImageField(upload_to='images/', null=True)
    file = models.FileField(upload_to='files/', null=True)
    view_count = models.IntegerField(default=0) # 정수형 타입
    created_at = models.DateTimeField(auto_now_add=True) # 날짜 및 시간 타입
    updated_at = models.DateTimeField(auto_now=True)