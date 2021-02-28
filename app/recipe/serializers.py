from rest_framework import serializers
from core.models import Recipe, Tag, Ingredient


class TagSerializer(serializers.ModelSerializer):
    """
    Serializer for tag objects
    """

    class Meta:
        model = Tag
        fields = ('id', 'name')
        extra_kwargs = {
            'id': {'read_only': True},
        }


class IngredientSerializer(serializers.ModelSerializer):
    """
    Serializer for ingredient objects
    """

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        extra_kwargs = {
            'id': {'read_only': True},
        }


class RecipeSerializer(serializers.ModelSerializer):
    """
    Serialize a recipe
    """
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingredient.objects.all(),
    )
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all(),
    )

    class Meta:
        model = Recipe
        fields = (
            'id', 'title', 'ingredients', 'tags',
            'price', 'link',
        )
        extra_kwargs = {
            'id': {'read_only': True},
        }
