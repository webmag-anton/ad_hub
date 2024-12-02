from django.contrib import admin
from .models import Ad, AdImage
from django.utils.html import format_html


class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category_list', 'price', 'created_at', 'updated_at', )
    search_fields = ('title', 'description')
    list_filter = ('categories', 'created_at', 'price')

    # Дополнительная настройка для отображения категорий в списке
    def category_list(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    category_list.short_description = 'Categories'


class AdImageAdmin(admin.ModelAdmin):
    list_display = ('ad', 'image_thumbnail')

    # Добавляем миниатюру изображения в админке
    def image_thumbnail(self, obj):
        return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
    image_thumbnail.short_description = 'Image'


admin.site.register(Ad, AdAdmin)
admin.site.register(AdImage, AdImageAdmin)