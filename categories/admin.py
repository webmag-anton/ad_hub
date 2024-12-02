from django.contrib import admin
from .models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'image')
    search_fields = ('name',)
    list_filter = ('parent',)


admin.site.register(Category, CategoryAdmin)