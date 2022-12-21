from django.urls import path
from . import views

# 添加index应用的路由
urlpatterns = [
    path('', views.index, name='index'),
]
