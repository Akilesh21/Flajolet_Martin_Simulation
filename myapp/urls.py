from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('index', views.index),
    path('simulation/', views.simulation, name='simulation'),
]
