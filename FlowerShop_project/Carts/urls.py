from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_detail,name="صفحه سبد خرید"),
    path('add/<int:plant_id>/', views.add_to_cart,name="add_to_cart"),
    path('manage/', views.manage_cart,name="manage_cart"),
    path('remove/<int:item_id>/', views.remove_from_cart,name="remove_from_cart"),
    path('remove/', views.remove_from_all_cart,name="remove_from_all_cart"),
    path('checkout/', views.checkoutt,name="checkout"),
]