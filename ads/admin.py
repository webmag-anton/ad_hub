from django.contrib import admin
from .models import Ad, AdImage, Category
from django.utils.html import format_html


class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category_list', 'price', 'condition', 'created_at', 'updated_at', )
    search_fields = ('title', 'description')
    list_filter = ('categories', 'created_at', 'price', 'condition')

    def category_list(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    category_list.short_description = 'Categories'

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        """Limit the selection of categories to subcategories only"""
        if db_field.name == "categories":
            # We get only those categories that have a parent (i.e. subcategories)
            kwargs["queryset"] = Category.objects.filter(parent__isnull=False)
        return super().formfield_for_manytomany(db_field, request, **kwargs)


class AdImageAdmin(admin.ModelAdmin):
    list_display = ('ad', 'image_thumbnail')

    def image_thumbnail(self, obj):
        return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
    image_thumbnail.short_description = 'Image'


admin.site.register(Ad, AdAdmin)
admin.site.register(AdImage, AdImageAdmin)