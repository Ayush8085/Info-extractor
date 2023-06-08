from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ImageFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static')
    image_text = models.TextField(null=True)