from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('1/', views.one, name="one"),
    path('2/', views.two, name="two"),
    path('3/', views.three, name="three"),
]