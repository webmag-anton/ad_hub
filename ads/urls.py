from . import views
from django.urls import path

urlpatterns = [
    path('my_ads/', views.my_ads, name='my_ads'),  
    path('user/<int:id>/', views.user_ads, name='user_ads'), 
    path('create/', views.create_ad, name='create_ad'),
    path('delete/<slug:slug>/', views.delete_ad, name='delete_ad'),
    path('edit/<slug:slug>/', views.edit_ad, name='edit_ad'),
    path('<slug:slug>/', views.get_ad, name='ad'),
]