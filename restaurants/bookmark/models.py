from django.db import models
from django.contrib.auth.models import User
from restaurant.models import Restaurant


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'restaurant')

    def __str__(self):
        return f"{self.user.username} bookmarks {self.restaurant.name}"
