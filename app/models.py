from django.db import models

class Item(models.Model):
    name=models.TextField(default=None)
    description=models.TextField(default=None)
    image=models.ImageField(upload_to='images/', default=None)
    def __str__(self):
	    return self.name