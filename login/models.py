from django.db import models

# Create your models here.

class Products (models.Model):
    image = models.CharField(max_length= 255, null=True)
    name = models.CharField(max_length= 50, null=True)
    price = models.IntegerField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


