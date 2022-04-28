from django.db import models


class Item(models.Model):
    type = models.CharField(max_length=50, default=None, null=True)
    item = models.CharField(max_length=100, default=None, null=True)
    image = models.ImageField(upload_to='images/', default=None, null=True)

    def __str__(self):
        return str(self.item)

class About(models.Model):
    company = models.CharField(max_length=1000, default=None, null=True)
    matt = models.CharField(max_length=1000, default=None, null=True)
    brian = models.CharField(max_length=1000, default=None, null=True)