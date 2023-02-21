from django.db import models
from django.contrib.auth.models import User
from restaurant.models import Restaurant

class Visit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date_visited = models.DateField()
    notes = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'restaurant')
        ordering = ('-created_on',)

    def __str__(self):
        return f'{self.user.username} visited {self.restaurant.name} on {self.date_visited}'
