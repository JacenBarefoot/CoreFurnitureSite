from django.db import models

class Item(models.Model):
    name: models.TextField()
    description: models.TextField()
    image: models.ImageField(upload_to='images/%Y/%m/%d')