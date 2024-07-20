# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edit/about/', views.edit_about_me, name='edit_about_me'),
    path('edit/skill/<int:skill_id>/', views.edit_skill, name='edit_skill'),
    path('edit/development/<int:development_id>/', views.edit_development, name='edit_development'),
]
