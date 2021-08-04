from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('view/', profile_view, name='profile_view'),
    path('edit/', profile_edit, name='profile_edit'),
    path('profile_id/<int:usr_id>', profile_view_by_id, name='profile_id'),
]