from django.db import models
from cuisine.models import Cuisine
from restaurant.models import Restaurant

class Dish(models.Model):
    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='dishes', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE, related_name='dishes')
