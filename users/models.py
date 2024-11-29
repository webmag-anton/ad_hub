from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=15, null=True, blank=True)
    avatar = CloudinaryField('avatar', null=True, blank=True)

    def __str__(self):
        return self.email
