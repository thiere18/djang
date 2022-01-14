from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('room/<int:pk>/',views.room,name='room'),
    path('create_room',views.create_room,name='create_room'),
    path('edit/<int:pk>/',views.edit_room,name="edit-room"),
    path('delete/<int:pk>/',views.delete_room,name="delete-room"),

]
