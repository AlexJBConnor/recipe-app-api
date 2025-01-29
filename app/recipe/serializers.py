# serializers for recipe apis

from rest_framework import Serializers
from core.models import Recipe

class RecipeSerializer(Serializers.ModelSerializer):
    # sewrializer for recipes

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']