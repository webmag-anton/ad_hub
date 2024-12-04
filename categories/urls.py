from . import views
from django.urls import path

urlpatterns = [
    path('', views.category_list, name='home'),
    # path('get-subcategories/<str:category_name>/', views.get_subcategories, name='get_subcategories'),
]