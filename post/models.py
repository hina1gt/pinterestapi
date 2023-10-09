from django.db import models
from django.contrib.auth.models import AbstractUser

class Category(models.Model):

    name = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name}'
    
class CustomUser(AbstractUser):

    def __str__(self):
        return f'{self.username}'

class Posts(models.Model):

    title = models.CharField(max_length=256, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='posts-images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    poster = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'
