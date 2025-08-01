from django.urls import path
from . import views                 

urlpatterns = [
    path('', views.index, name='index'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'), 
    path('cart/', views.view_cart, name='view_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order_success/', views.order_success, name='order_success'),
]
