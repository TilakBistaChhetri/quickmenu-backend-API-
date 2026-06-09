




from django.contrib.auth.models import User
from django.db import models
from .restaurant import Restaurant

class RestaurantUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    