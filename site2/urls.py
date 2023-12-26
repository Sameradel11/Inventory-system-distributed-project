"""
URL configuration for databases project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
app_name='site2'

urlpatterns = [
    path('db/', views.db_table, name='db_table'),
    path('db/add/', views.db_table_add, name='db_table_add'),
    path('db/update/', views.db_table_update, name='db_table_update'),

        # URLs for page 2
    path('location/', views.location, name='location'),
    path('location/add/', views.location_add, name='location_add'),
    path('location/update/<str:pk>', views.location_update, name='location_update'),
    path('location/delete/<str:pk>',views.location_delete,name='location_delete'),

        # URLs for page 3
    path('inventory/', views.inventory, name='inventory'),
    path('inventory/add/', views.inventory_add, name='inventory_add'),
    path('inventory/update/<str:pk>', views.inventory_update, name='inventory_update'),
    path('inventory/delete/<str:pk>',views.inventory_delete,name='inventory_delete'),

        # URLs for page 4 - Product folder
    path('product/', views.product, name='product'),
    path('product/add/', views.product_add, name='product_add'),
    path('product/update/<str:pk>', views.product_update, name='product_update'),
    path('product/delete/<str:pk>',views.product_delete,name='product_delete'),


    path('productinventory_add/<str:pk>',views.product_inventory_add, name='product_inventory_add'),
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
]