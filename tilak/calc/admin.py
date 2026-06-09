

from django.contrib import admin
from .models import Category

admin.site.register(Category)
  


from django.contrib import admin
from calc.models import Restaurant, RestaurantUser
admin.site.register(Restaurant)
admin.site.register(RestaurantUser)