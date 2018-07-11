from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from api.models import Food, Meal
from api.serializers import FoodSerializer, MealSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
import json


from IPython import embed

class FoodViews(viewsets.ViewSet):

    def list(self, request):
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)

    def retrieve(self, request, food_id=None):
        food = get_object_or_404(Food, id=food_id)
        serializer = FoodSerializer(food, many=False)
        return Response(serializer.data)

    def create(self, request):
        food_attrs = request.data['food']
        if 'name' in food_attrs.keys() and 'calories' in food_attrs.keys():
            food = Food.objects.create(name=food_attrs['name'], calories=food_attrs['calories'])
            serializer = FoodSerializer(food)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, food_id=None):
        food = get_object_or_404(Food, id=food_id)
        food_attrs = request.data['food']
        if 'name' in food_attrs.keys() and 'calories' in food_attrs.keys():
            food.name = food_attrs['name']
            food.calories=food_attrs['calories']
            food.save()
            serializer = FoodSerializer(food)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, food_id=None):
        food = get_object_or_404(Food, id=food_id)
        food_attrs = request.data['food']
        if 'name' in food_attrs.keys() and 'calories' in food_attrs.keys():
            food.name = food_attrs['name']
            food.calories=food_attrs['calories']
            food.save()
            serializer = FoodSerializer(food)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, food_id=None):
        food = get_object_or_404(Food, id=food_id)
        food.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class MealViews(viewsets.ViewSet):

    def list(self, request):
        meals = Meal.objects.all()
        serializer = MealSerializer(meals, many=True)
        return Response(serializer.data)

    def retrieve(self, request, meal_id=None):
        meal = get_object_or_404(Meal, id=meal_id)
        serializer = MealSerializer(meal, many=False)
        return Response(serializer.data)


class MealFoodViews(viewsets.ViewSet):

    def create(self, request, meal_id=None, food_id=None):
        meal = get_object_or_404(Meal, id=meal_id)
        food = get_object_or_404(Food, id=food_id)
        meal.foods.add(food)
        message = { 'message': f'Successfully added {food.name} to {meal.name}' }
        return Response(message, status=status.HTTP_201_CREATED)

    def destroy(self, request, meal_id=None, food_id=None):
        meal = get_object_or_404(Meal, id=meal_id)
        food = get_object_or_404(Food, id=food_id)
        meal.foods.remove(food)
        message = { 'message': f'Successfully removed {food.name} from {meal.name}' }
        return Response(message, status=status.HTTP_204_NO_CONTENT)
