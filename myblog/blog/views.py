# render는 '템플릿을 불러오는 것', redirect는 'URL로 이동하는 것(해당 URL의 views 함수를 실행하는 것)'.
from django.shortcuts import render, redirect, get_object_or_404 # "django.shortcuts 패키지에 있는 render 함수 등을 사용하로독 하겄따잉!"
from .models import *

# 함수와 함수 사이는 두 줄 간격이 좋다!
# 프로그래밍에서 =는 같다는 뜻이 아니라 대입한다는 뜻!!!!! 같다는 의미로 사용할 땐 ==를 쓴다.

def main(request): # "이걸 main이라는 함수로 명명하겠다! request를 인자로 받는다!"
    all_posts = Post.objects.all() # "Post 클래스의 모든 항목들을 all_posts(변수)라고 부르겠다!"
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
        Post.objects.create(title=post_title, writer=post_writer, content=post_content, image=post_image)
    return redirect('blog:main') # blog:main이라는 URL로 이동 -> blog.views에서 main 함수 실행 -> blog/main.html을 render


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
    return render(request, 'blog/show.html', {'post': post})


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