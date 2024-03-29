"""
URL configuration for web5 project.

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
    1. Import the incdjango-admin startproject myprojectlude() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('depart/list/', views.depart_list),
    path('depart/add/', views.depart_add),
    path('depart/delete/', views.depart_delete),
    path('depart/<int:nid>/ebit/', views.depart_ebit),
    #

    path('role/list/', views.role_list),
    path('role/add/', views.role_add),
    path('role/delete/', views.role_delete),
    path('role/<int:nid>/ebit/', views.role_ebit),

    path('user/list/', views.user_list),
    path('user/add/', views.user_add),
    path('user/<int:nid>/delete/', views.user_delete),
    path('user/<int:nid>/ebit/', views.user_ebit),
]
