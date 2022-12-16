from django.urls import path
from . import views

urlpatterns = [
    path('addcart/', views.add_to_cart, name='addcart'),
    path('cart/', views.get_cart, name='cart'),
    path('delcart/', views.delete_cart, name='delcart'),
    path('finalorder/', views.finalorder, name='finalorder'),
    path('conforder/', views.conforder, name='conforder'),
]
