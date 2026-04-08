from rest_framework import serializers
from calc.models.home.about.about import About

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['id', 'title', 'description']