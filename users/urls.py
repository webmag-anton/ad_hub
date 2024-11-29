from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_page, name='home'),   
    path('profile/', views.profile_page, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]