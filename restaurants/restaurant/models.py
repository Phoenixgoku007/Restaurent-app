from django.db import models
from django.contrib.auth.models import User
from cuisine.models import Cuisine

class Restaurant(models.Model):
    
    title = models.CharField(max_length=200, default='')
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.PROTECT)
    cost_for_two = models.DecimalField(max_digits=6, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    timings = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def save(self, *args, **kwargs):
        self.cuisine_id = self.cuisine.id
        super().save(*args, **kwargs)
    VEG = 'VEG'
    VEGAN = 'VEGAN'
    NON_VEG = 'NON-VEG'
    FOOD_TYPE_CHOICES = (
        (VEG, 'Veg'),
        (VEGAN, 'Vegan'),
        (NON_VEG, 'Non-Veg')
    )
    food_type = models.CharField(
        max_length=10,
        choices=FOOD_TYPE_CHOICES,
        default=VEG
    )
    class Meta:
        app_label = 'restaurant'

