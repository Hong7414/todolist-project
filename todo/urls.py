from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.todo, name='todo'),
    path('todo/<int:id>', views.view, name='view'),
    path('create/', views.create, name='create'),
    path('completed/', views.completed, name='completed'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('completed/<int:id>', views.completed_by_id, name='completed_by_id'),

]
