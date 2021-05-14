from django.urls import path
from .views import cartcrud
from .views import CartItemCreate, CartItemsList,OrderItems

urlpatterns = [
    path('create/<int:pk>/',cartcrud.createCartItem, name='create_item'),
    path('cart_items/<int:pk>/',CartItemsList.as_view(), name='cart_items'),
    path('update_order/<int:pk>/', cartcrud.updateCartItem, name="update_item"),
    path('delete_order/<int:pk>/', cartcrud.deleteCartItem, name="delete_item"),
    path('orders/<int:pk>/', OrderItems.as_view(), name="orders"),
]