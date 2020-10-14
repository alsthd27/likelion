from django.urls import path
from .views import *

app_name = 'blog' # app_name 설정하는 이유: 서로 다른 앱에서 동일한 이름의 템플릿 파일이 생성될 수도 있으니 app_name으로 구분하는 것.
urlpatterns = [
    path('', main, name="main"), # urls.py에서 name 설정하면 템플릿 태그 활용 가능.
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('<int:post_id>/', show, name="show"), # <int:id>는 id라는 이름을 가진 integer 값을 말함.
    path('<int:post_id>/edit/', update, name="update"),
    path('<int:post_id>/delete/', delete, name="delete"),
    path('<int:post_id>/create_comment/', create_comment, name="create_comment"),
    path('<int:post_id>/post_like/', post_like, name="post_like"),
    path('like_list/', like_list, name="like_list"),
]