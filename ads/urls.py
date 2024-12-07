from . import views
from django.urls import path

urlpatterns = [
    path('my_ads/', views.my_ads, name='my_ads'),  
    path('create/', views.create_ad, name='create_ad'),
    path('delete/<slug:slug>/', views.delete_ad, name='delete_ad'),
    path('user/<int:id>/', views.user_ads, name='user_ads'), 
    path('<slug:slug>/', views.get_ad, name='ad'),
]