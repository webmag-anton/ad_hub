from django.shortcuts import render
import json
from .models import Category

# Create your views here.
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