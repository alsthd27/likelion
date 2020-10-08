from django.urls import path
from .views import main, one, two, three, new

app_name = 'blog' # app_name 설정 시 템플릿 태그에도 입력해야 함.
urlpatterns = [
    path('', main, name="main"),
    path('1/', one, name="one"), # urls.py에서 name 설정하면 템플릿 태그 활용 가능.
    path('2/', two, name="two"),
    path('3/', three, name="three"),
    path('new/', new, name="new"),
]