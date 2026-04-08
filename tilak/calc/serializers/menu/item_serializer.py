from rest_framework import serializers
from calc.models.menu.item import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        # Exclude categoryId or category_name completely
        fields = [
            'id',
            'item_name',
            'price',
            'availability',
            'description',
            'image',
            'created_at',
            'updated_at',
        ]