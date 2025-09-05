from rest_framework import serializers
from .models import Category, Dish, Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('email', 'name', 'comment',)


class DishSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'price', 'image')


class DishSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Dish
        fields = ('id', 'name', 'price', 'image', 'category', 'reviews')


class DishDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    reviews = ReviewSerializer(many=True, read_only=True)
    similar_dishes = serializers.SerializerMethodField()

    class Meta:
        model = Dish
        fields = ('id', 'name', 'price', 'is_available', 'composition', 'image', 'category', 'reviews', 'similar_dishes')

    def get_similar_dishes(self, obj):
        queryset = Dish.objects.filter(category=obj.category).exclude(id=obj.id)[:5]
        return DishSimpleSerializer(queryset, many=True).data
