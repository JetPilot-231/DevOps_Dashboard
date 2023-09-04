# dashboard_app/urls.py
from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    # Добавьте другие маршруты, как необходимо
]
