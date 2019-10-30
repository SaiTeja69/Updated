from django.urls import path
from .views import post_home,new_post,view_post,delete_post,edit_post

urlpatterns=[

path('',post_home),
path('new_post/',new_post),
path('<str:slug>',view_post),
path('<str:slug>/edit/',edit_post),

path('<str:slug>/delete/',delete_post),



]
