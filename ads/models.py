from django.db import models
from cloudinary.models import CloudinaryField
from users.models import User
from categories.models import Category


class Ad(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads')
    categories = models.ManyToManyField(Category, related_name='ads')
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class AdImage(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image')

    def __str__(self):
        return f"Image for Ad title: {self.ad.title}"