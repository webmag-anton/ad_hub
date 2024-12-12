from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('profile/', include('users.urls'), name='profile-urls'),
    path('ads/', include('ads.urls'), name='ads-urls'),
    path('', include('categories.urls'), name='categories-urls'),
]
