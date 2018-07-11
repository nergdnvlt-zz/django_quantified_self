import json
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from api.models import Food, Meal
from IPython import embed

class MealFoodsEndpointTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.apple  = Food.objects.create(name="apple", calories=100)
        self.ramen  = Food.objects.create(name="delicious ramen", calories=888)
        self.banana = Food.objects.create(name="banana", calories=100)

        self.breakfast = Meal.objects.create(name='Breakfast')
        self.snack = Meal.objects.create(name='Snack')


    def test_posts_food_to_meal(self):
        response = self.client.post(f'/api/v1/meals/{self.breakfast.id}/foods/{self.apple.id}')

        self.assertEqual(response.data['message'], "Successfully added apple to Breakfast")

    def test_add_mealfood_sad_path_no_meal(self):
        response = self.client.post(f'/api/v1/meals/101/foods/{self.apple.id}')

        self.assertEqual(response.status_code, 404)

    def test_add_mealfood_sad_path_no_food(self):
        response = self.client.post(f'/api/v1/meals/{self.breakfast.id}/foods/1001')

        self.assertEqual(response.status_code, 404)

    def test_remove_food_from_meal(self):
        self.breakfast.foods.add(self.apple)
        response = self.client.delete(f'/api/v1/meals/{self.breakfast.id}/foods/{self.apple.id}')

        self.assertEqual(response.data['message'], "Successfully removed apple from Breakfast")

    def test_remove_mealfood_sad_path_no_food(self):
        self.breakfast.foods.add(self.apple)
        response = self.client.delete(f'/api/v1/meals/1001/foods/{self.apple.id}')

        self.assertEqual(response.status_code, 404)

    def test_remove_mealfood_sad_path_no_food(self):
        self.breakfast.foods.add(self.apple)
        response = self.client.delete(f'/api/v1/meals/{self.breakfast.id}/foods/1001')

        self.assertEqual(response.status_code, 404)
