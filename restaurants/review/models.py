from django.db import models
from django.contrib.auth import get_user_model
from restaurant.models import Restaurant

User = get_user_model()


class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review {self.id} for {self.restaurant.name} by {self.user.username}'
