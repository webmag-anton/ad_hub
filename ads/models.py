from django.utils.text import slugify
from django.db import models
from django.core.exceptions import ValidationError
import uuid # python module
from cloudinary.models import CloudinaryField
from users.models import User
from categories.models import Category


class Ad(models.Model):
    CONDITION_CHOICES = [
        ('new', 'New'),
        ('used', 'Used'),
    ]

    slug = models.SlugField(max_length=200, unique=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads')
    categories = models.ManyToManyField(Category, related_name='ads')
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    location = models.CharField(max_length=100, default='Ireland, co. Cork, Cork')
    condition = models.CharField(
        max_length=4,
        choices=CONDITION_CHOICES,
        default='new',
        null=False,
        blank=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean_categories(self):
        # Checking that ad categories are subcategories
        for category in self.categories.all():
            if not category.parent:
                raise ValidationError(f"Cannot create Ad in the top-level category '{category.name}'. Please choose a subcategory.")

    def save(self, *args, **kwargs):
        # Generate a unique slug if it is missing
        if not self.slug:
            unique_id = uuid.uuid4().hex[:8]
            self.slug = slugify(f"{self.title}-{unique_id}")
        # Save the object to ensure it has an ID
        super().save(*args, **kwargs)
        # Run the clean method to validate categories
        self.clean_categories()   
        # Add categories (needed since this is a Many-to-Many relationship)
        self.categories.add(*self.categories.all())

    def __str__(self):
        return self.title


class AdImage(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image')

    def __str__(self):
        return f"Image for Ad title: {self.ad.title}"