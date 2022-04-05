from django.db import models

class Admin(models.Model):
    username: models.TextField()
    password: models.TextField()
    email: models.EmailField()
    phone: models.BigIntegerField()

class Item(models.Model):
    name: models.TextField()
    description: models.TextField()
    image: models.URLField()
    