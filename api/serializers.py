from rest_framework import serializers
from api.models import Food
from api.models import Meal


class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = ('id', 'name', 'calories')


class MealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meal
        fields = ('id', 'name', 'foods')
