from django.shortcuts import render
from .models import Category

# Create your views here.
def home_page(request):
    categories = Category.objects.all()
    context = {'categories': categories}

    return render(request, 'categories/index.html', context)