from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.custom_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('edit/about/', views.edit_about_me, name='edit_about_me'),
    path('edit/skill/<int:skill_id>/', views.edit_skill, name='edit_skill'),
    path('edit/development/<int:development_id>/', views.edit_development, name='edit_development'),
    path('add_skill/', views.add_skill, name='add_skill'),
    path('add_development/', views.add_development, name='add_development')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)









# from django.urls import path
# from . import views
# from django.contrib.auth.views import LogoutView
# from django.conf import settings
# from django.conf.urls.static import static
# from django.urls import path


# urlpatterns = [
#     path('', views.home, name='home'),
#     path('login/', views.custom_login, name='login'),
#     path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
#     path('edit/about/', views.edit_about_me, name='edit_about_me'),
#     path('edit/skill/<int:skill_id>/', views.edit_skill, name='edit_skill'),
#     path('edit/development/<int:development_id>/', views.edit_development, name='edit_development'),
#     path('add_skill/', views.add_skill, name='add_skill'),
#     path('add_development/', views.add_development, name='add_development')
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
