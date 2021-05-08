from django.urls import path
from . views import ProductList,ProductDetail,ProductCreate,ProductUpdate,ProductDelete,GetAllUserProducts,temp
urlpatterns = [
    path('',ProductList.as_view(),name='products'),
    path('product_create/',ProductCreate.as_view(),name='product_create'),
    path('product_update/<int:pk>/',ProductUpdate.as_view(),name='product_update'),
    path('product_delete/<int:pk>/',ProductDelete.as_view(),name='product_delete'),
    path('product/<int:pk>/',ProductDetail.as_view(),name='product'),
    path('products/<int:pk>', GetAllUserProducts.as_view(), name='all_user_products'),
    path('basic/', temp, name='basic'),


]
