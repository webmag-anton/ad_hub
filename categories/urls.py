from . import views
from django.urls import path

urlpatterns = [
    path('', views.category_list, name='home'),
    path('category/<str:category_name>/', views.ads_by_category, name='ads_by_category'),
    # path('get-subcategories/<str:category_name>/', views.get_subcategories, name='get_subcategories'),
]