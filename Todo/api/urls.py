from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.AppOverview,name="overview"),
    path('task-list/',views.noteslist,name='task-list'),
    path('task-detail/<str:pk>/',views.notesdetails,name='task-detail'),
    path('task-create/',views.notescreate,name='task-create'),
    path('task-update/<str:pk>/',views.notesupdate,name='task-update'),
    path('task-delete/<str:pk>/',views.notesdelete,name='task-delete'),
    
]
