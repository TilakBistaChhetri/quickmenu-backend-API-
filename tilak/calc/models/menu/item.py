from django.db import models
from calc.models.menu.category import Category

class Item(models.Model):
    categoryId = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='items'
    )
    item_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='items/', default='items/default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item_name} - {self.categoryId.name}"


    
   # auto_now_add=True means jati bela database maa first time record create hunxa teti belako date auto set hunxa
   # auto_now = True means jati bela pani database maa record save hunxa teti bela ko date auto update hunxa.
   # ForeignKey le 2 ota table Category and Item table laai connect garne kaam garxa. many to one relation like one category but many items.
   # on_delete =models.CASADE, CASADE vannale whne category remove hunxa teo vitra ko all item remove hunxa.
   #related_name='items' yo reverse relationship ho, category baat sidhai tes vitra ko item lin sakinxa.