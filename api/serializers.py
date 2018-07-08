from rest_framework import serializers
from api.models import Food
from api.models import Meal


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('id', 'name', 'calories')


class MealSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(many=True)

    class Meta:
        model = Meal
        fields = ('id', 'name', 'foods')
