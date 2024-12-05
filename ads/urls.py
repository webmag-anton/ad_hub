from . import views
from django.urls import path

urlpatterns = [
    path('my_ads', views.my_ads, name='my_ads'),   
    path('<slug:slug>/', views.get_ad, name='ad')
]