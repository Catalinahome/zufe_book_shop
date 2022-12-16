from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='book'),
    path('search_book', views.search, name='search'),
]
