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
    '''
    N:M 관계이므로 ManyToManyField 활용. User(M) : Post(N)
    게시글에 좋아요가 하나도 없을 수 있으니 blank=True
    through는 어느 모델을 통해 관계가 이루어지는지(정의되는지) 설정하는 것. Like 모델을 통해 User와 Post의 좋아요(M:N) 관계가 정의되고 있다.
    '''
    like_user_set = models.ManyToManyField(User, blank=True, related_name="like_user_set", through="Like")

    @property # 데코레이터에 property를 붙이면 get method를 선언.
    def like_count(self): # 얘는 게시글에 달린 좋아요의 갯수를 세는 함수다. self는 모델의 객체를 의미한다. Post가 아니라 post에 달린 좋아요 갯수를 셀 거니까.
        '''
        아쒸발이해가잘안된당
        일단 Like 모델링 (Post 객체와 User 객체를 한 쌍으로 연결 / post와 user를 Like 모델에 저장) ->
        지금 이 Post 모델에 like_user_set 속성 추가 (User 모델과 M:N 관계 형성 / Like 모델의 데이터를 Post와 User의 M:N 관계와 연결) ->
        데코레이터로 지금 이 like_count 함수 생성 (post에 좋아요 표시를 한 user 데이터 갯수를 카운트 / 결국 Like 모델 객체의 갯수를 카운트)   
        '''
        return self.like_user_set.count()


class Like(models.Model): # User와 Post 두 모델의 데이터를 저장할 중간(intermediate) 모델
    user = models.ForeignKey(User, on_delete=models.CASCADE) # user(1) : Like(N) 한 명의 사용자가 여러 게시글에 좋아요를 달 수 있다.
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # post(1) : Like(N) 한 게시글에 여러 개의 좋아요가 달릴 수 있다.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: # 모델 안에 메타데이터를 추가할 수 있다. 모델 단위에서 설정할 수 있는 옵션이라 생각하면 된다. 모델 필드 아래쪽에 반드시 한 줄 공백을 줘야 한다.
        unique_together = (('user', 'post')) #unique_together는 '함께 유일해야 하는 필드의 쌍'을 의미한다. A 유저가 B 게시글에 누른 좋아요가 중복될 수는 없으니까.


class Comment(models.Model):
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    '''
    Post가 1, Comment가 N이니까, Comment에 ForeignKey 추가. (한 게시글에 여러 댓글이 달리니께~~~)
    N에서 1로 접근할 때는 바로 접근 가능! (1은 말 그대로 딱 한 개밖에 없으니까!)
    근데 1에서 N에 접근할 때는 set을 반드시 사용해야 함! (N은 말 그대로 존나 여러 개니까!)
    related_name은 set과 비슷하게 '역추적 할 때 사용되는 속성'!
    ForeignKey의 related_name은 N에 접근하기 위한 이름(N을 가르키는 이름)이므로 복수형으로 지어라~!~!~!~!!

    # Comment에서 Post로 접근할 때(특정 댓글이 어떤 게시글에 달려있는지 확인할 때) 터미널 예시
    >>> from comments.models import Comment

    >>> comment = Comment.objects.get(pk=특정값)
    >>> comment.post

    # Post에서 Comment로 접근할 때(특정 게시글에 달린 댓글들을 확인할 때) 터미널 예시
    >>> from posts.models import Post

    >>> post = Post.objects.get(pk=특정값)
    >>> post.comment_set
    >>> post.comment_set.add()
    >>> post.comment_set.count()

    # 근데 만약 related_name을 설정해줬다면?
    >>> from posts.models import Post

    >>> post = Post.objects.get(id=특정값)
    >>> post.comments
    하면 set을 쓰지 않고도 post.comments_set의 효과를 볼 수 있음.
    '''
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)