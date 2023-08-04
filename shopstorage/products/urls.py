from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
]