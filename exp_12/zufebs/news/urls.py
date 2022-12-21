from django.urls import path
from . import views

# 添加news应用的路由
urlpatterns = [
    path('', views.index, name='news'),
]
