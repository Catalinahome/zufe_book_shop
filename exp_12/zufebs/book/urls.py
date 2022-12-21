from django.urls import path
from . import views

# 添加book应用路由
urlpatterns = [
    path('', views.index, name='book'),
    path('search_book', views.search, name='search'),
]
