from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.shop, name='shop'),
    path('<int:pk>/', views.product_details, name='product_details'),
]