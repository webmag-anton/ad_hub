from django.shortcuts import render, get_object_or_404
import json
from .models import Category
from ads.models import Ad


def category_list(request):
    top_level_categories = Category.objects.filter(parent__isnull=True)
    
    categories_data = []
    for category in top_level_categories:
        subcategories = category.get_subcategories()
        categories_data.append({
            'name': category.name,
            'image': category.image.url if category.image else None,
            'subcategories': [{'name': subcategory.name} for subcategory in subcategories]
        })

    # serialise data to JSON because of cloudinary images url
    context = {'categories_data_json': json.dumps(categories_data)} 
    return render(request, 'categories/index.html', context)


def ads_by_category(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    ads = Ad.objects.filter(categories=category)
    ads_count = ads.count()
    
    context = {
        'category': category,
        'ads': ads,
        'ads_count': ads_count
    }
    return render(request, 'categories/ads_by_category.html', context)