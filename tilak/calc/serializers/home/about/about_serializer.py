# calc/serializers/home/about/about_serializer.py
from rest_framework import serializers
from calc.models.home.about.about import About

class AboutSerializer(serializers.ModelSerializer):
    why_choose_us = serializers.ListField(
        child=serializers.CharField()
    )

    class Meta:
        model = About
        fields = ['title', 'description', 'why_choose_us']