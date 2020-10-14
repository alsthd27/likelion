from django.db import models
from django.contrib.auth.models import User # 유저를 관리하기 위해 Django의 User 모델을 import

# Django에서 model은 class 개념, models의 Model을 상속받는다!!!!!

class Post(models.Model):
    title = models.CharField(max_length=50, null=False) # 짧은 문자열 필드
    '''
    User를 writer라는 이름으로 불러오고 Post와 1:N 관계(ForeignKey)로 연결
    on_delete=models.CASCADE는 유저(1)가 삭제되면 게시글(N)도 삭제되도록 하는 것!
    CASCADE 말고 PROTECT, SET_NULL(null=True가 설정돼있어야 함), SET_DEFAULT(default값이 설정돼있어야 함), SET()(대체할 값이나 함수 입력), DO_NOTHING을 입력할 수 있음.
    User 모델 사용 전에 작성된 게시글은 유저가 존재하지 않으므로 null=True
    '''
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField() # 긴 문자열 필드
    image = models.ImageField(upload_to='images/', null=True)
    file = models.FileField(upload_to='files/', null=True) # file은 일단 추가만 해놨고 사용하진 않고 있음.
    view_count = models.IntegerField(default=0) # 정수형 타입
    created_at = models.DateTimeField(auto_now_add=True) # 날짜 및 시간 타입
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments') # Post가 1, Comment가 N이니까, Comment에 ForeignKey 추가. (한 게시글에 여러 댓글이 달리니께~~~)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)