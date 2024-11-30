from . import views
from django.urls import path

urlpatterns = [ 
    path('', views.profile_page, name='profile'),
    path('edit/', views.edit_profile, name='edit_profile'),
]