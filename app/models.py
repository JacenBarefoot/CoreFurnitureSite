from django.db import models


class Item(models.Model):
    category = models.CharField(max_length=50, default=None, null=True)
    item = models.CharField(max_length=100, default=None, null=True)
    image = models.ImageField(upload_to='images/', default=None, null=True)

    def __str__(self):
        return str(self.item)

class About(models.Model):
    company = models.CharField(max_length=1000, default=None, null=True)
    matt = models.CharField(max_length=1000, default=None, null=True)
    matt_picture = models.ImageField(upload_to='images/', default=None, null=True)
    bryan = models.CharField(max_length=1000, default=None, null=True)
    bryan_picture = models.ImageField(upload_to='images/', default=None, null=True)

class Testimony(models.Model):
    name = models.CharField(max_length=50, null=True, default=None)
    body = models.CharField(max_length=500, default=None, null=True)

class Footer(models.Model):
    address = models.CharField(max_length=100, null=True, default=None)
    phone = models.CharField(max_length=20, null=True, default=None)
    email = models.CharField(max_length=50, null=True, default=None)

class Contract_info(models.Model):
    body = models.CharField(max_length=300, null=True, default=None)
