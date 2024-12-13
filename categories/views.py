from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
import json
from .models import Category
from ads.models import Ad


"""
User can open the page with a list of all categories and subcategories.
"""
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


"""
User can open the category page with a list of all 
ads in this category. Ads are sorted by creation date.
"""
def ads_by_category(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    ads = Ad.objects.filter(categories=category).order_by('-created_at')
    ads_count = ads.count()
    paginator = Paginator(ads, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'category': category,
        'ads': ads,
        'ads_count': ads_count,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    }
    return render(request, 'categories/ads_by_category.html', context)