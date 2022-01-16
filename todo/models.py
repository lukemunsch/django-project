from django.db import models


# Create your models here.
class Item(models.Model):
    """
    Creates the model class for the item table
    """
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        """Change the default value item object to item name specific"""
        return self.name
