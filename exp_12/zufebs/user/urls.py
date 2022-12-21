from django.urls import path
from . import views


# 添加user应用路由
urlpatterns = [
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='reg'),
]
