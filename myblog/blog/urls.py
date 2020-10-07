from django.urls import path
from . import views

app_name = 'blog' # app_name 설정 시 템플릿 태그에도 입력해야 함.
urlpatterns = [
    path('', views.main),
    path('1/', views.one, name="one"), # urls.py에서 name 설정하면 템플릿 태그 활용 가능.
    path('2/', views.two, name="two"),
    path('3/', views.three, name="three"),
]