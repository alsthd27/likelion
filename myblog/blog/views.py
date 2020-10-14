# render는 '템플릿을 불러오는 것', redirect는 'URL로 이동하는 것(해당 URL의 views 함수를 실행하는 것)'.
from django.shortcuts import render, redirect, get_object_or_404 # "django.shortcuts 패키지에 있는 render 함수 등을 사용하로독 하겄따잉!"
from .models import *
from django.contrib.auth.decorators import login_required # @login_required 데코레이터를 사용하기 위해 import.

# 함수와 함수 사이는 두 줄 간격이 좋다!
# 프로그래밍에서 =는 같다는 뜻이 아니라 대입한다는 뜻!!!!! 같다는 의미로 사용할 땐 ==를 쓴다.

def main(request): # "이걸 main이라는 함수로 명명하겠다! request를 인자로 받는다!"
    '''
    "Post 클래스의 모든 항목들을 all_posts(변수)라고 부르겠다!"
    order_by('-created_at')은 최신 생성순(내림차순)으로 정렬하겠다는 것.
    '''
    all_posts = Post.objects.all().order_by('-created_at')
    # Django에서 render의 세 번째 인자는 Python의 딕셔너리 타입 값을 넣어줘야 함.
    return render(request, 'blog/main.html', {'posts': all_posts}) # "request의 변수(all_posts)를 posts라는 이름으로 명명하고, 해당 request를 render 함수를 활용해 blog/main.html으로 return하겠다!"


def new(request):
    return render(request, 'blog/new.html')


def create(request):
    if request.method == "POST":
        post_title = request.POST.get('title')
        post_writer = request.user # 요청을 보낸 user의 정보!
        post_content = request.POST.get('content')
        post_image = request.FILES.get('image')
        # =의 왼쪽은 Post 모델의 속성, =의 오른쪽은 해당 속성에 들어갈 변수 이름
        Post.objects.create(title=post_title, writer=post_writer, content=post_content, image=post_image)
    return redirect('blog:main') # blog:main이라는 URL로 이동 -> blog.views에서 main 함수 실행 -> blog/main.html을 render


def create_comment(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=post_id)
        comment_writer = request.user
        comment_content = request.POST.get('content')
        Comment.objects.create(writer=comment_writer, content=comment_content, post=post)
        # return redirect('blog:show', post.pk)
    return redirect('blog:show', post_id)
    '''
    return redirect('blog:show', post.pk)가 아니라
    return redirect('blog:show', post_id)인 이유는?!

    만약에 post.id로 작성을 하면, POST 방식의 요청이 아닌 경우에는 post에 게시글이 담기질 않으니 post.id를 사용할 수 없는 상태가 된다.
    따라 에러가 발생하게 되므로 유저가 당황하지 않도록 post.pk가 아닌 요청에서 받아온 post_id를 그대로 작성한 것.

        return redirect('blog:show', post.pk)
    return redirect('blog:show', post_id)
    이렇게 써도 되긴 하는데, 굳이 이렇게 쓸 필요가 없는 것.
    '''


def show(request, post_id): # 특정 글을 가져오려면 해당 글의 고유 id를 알아야겠지??
    post = Post.objects.get(pk=post_id) # pk = primary key (id와 비슷한 뜻)
    ''' 요렇게 쓴 걸
    incresed_view_count = post.view_count + 1 # 조회수를 하나 늘리고
    post.view_count = incresed_view_count # 하나 늘린 조회수를 다시 원래 뷰 카운트에 대입
    post.save() # 그리고 해당 Post 객체를 저장
    '''
    ''' 요렇게 줄일 수 있고
    post.view_count = post.view_count + 1
    post.save()
    '''
    ''' 요렇게까지 줄일 수 있다.
    a += b는 a = a + b를 의미한다.
    즉, post.view_count += 1은 post.view_count = post.view_count + 1을 의미한다.
    '''
    post.view_count += 1
    post.save()
    all_comments = post.comments.all().order_by('-created_at') # Comment 모델링할 때 related_name으로 설정했던 그 comments를 쓴 것.
    return render(request, 'blog/show.html', {'post': post, 'comments': all_comments})


def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id) # get_object_or_404는 해당 객체가 존재하면 불러오고 존재하지 않으면 404 에러를 낸다.
    if request.method == "POST":
        post.title = request.POST['title'] # 딕셔너리 자료형으로서 'key에 해당하는 value를 가져오는 방법'은 두 가지가 있다. 하나는 변수명.get('key')이고 다른 하나는 변수명['key']이다.
        post.content = request.POST['content']
        post.image = request.FILES.get('image') # 파일 객체를 불러올 때는 request.FILES.get()을 사용한다.
        post.save()
        return redirect('blog:show', post.pk)
    return render(request, 'blog/edit.html', {'post': post})


def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('blog:main')


@login_required
def post_like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user in post.like_user_set.all(): # post와 user의 모든 쌍들(게시글에 좋아요를 누른 모든 유저들) 중 요청을 보낸 유저가 포함돼있다면
        post.like_user_set.remove(request.user) # 이미 그 유저는 좋아요를 눌렀다는 뜻이므로, 이 요청은 좋아요를 취소해달라는 거겠지? 그니까 remove
    else:
        post.like_user_set.add(request.user) # 그게 아니면 add
    if request.GET.get('redirect_to') == 'show': # 만약 요청이 redirect_to=show라는 GET 방식으로 왔다면
        return redirect('blog:show', post_id) # post_id에 해당하는 show로 redirect
    elif request.GET.get('redirect_to') == 'like_list':
        return redirect('blog:like_list')
    else:
        return redirect('blog:main') # 아니면 main으로 redirect


@login_required
def like_list(request):
    likes = Like.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'blog/like_list.html', {'likes': likes})