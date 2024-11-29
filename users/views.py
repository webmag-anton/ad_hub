from django.shortcuts import render
from django.views.generic import TemplateView
from .models import User


def home_page(request):
    users = User.objects.all()
    context = {'users': users}

    return render(request, 'ads/index.html', {'users': users})
    