




from rest_framework import serializers
from calc.models.item import Item

class ItemSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = Item
    #     # Exclude categoryId or category_name completely
    #     fields = [
    #         'id',
    #         'categoryId',
    #         'item_name',
    #         'price',
    #         'availability',
    #         'description',
    #         'image',
    #         'created_at',
    #         'updated_at',
    #     ]


      class Meta:
            model = Item
            fields = [
                "id",
                "name",
                "description",
                "price",
                "categoryId",
                "image",
            ]
        


    
    # class ItemSerializer(serializers.ModelSerializer):
    #   class Meta:
    #     model = Item
    #     fields = [
    #         "id",
    #         "name",
    #         "description",
    #         "price",
    #         "categoryId",
    #         "image",
    #     ]