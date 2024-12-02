from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='subcategories', on_delete=models.CASCADE
    )
    image = CloudinaryField('image', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_subcategories(self):
        return self.subcategories.all()