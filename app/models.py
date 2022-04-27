from django.db import models


class Item(models.Model):
    type = models.CharField(max_length=50, default=None, null=True)
    item_no = models.IntegerField(default=None, null=True)
    image = models.ImageField(upload_to='images/', default=None, null=True)

    def __str__(self):
        return str(self.item_no)