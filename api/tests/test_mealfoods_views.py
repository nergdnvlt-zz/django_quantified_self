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



    # def test_gets_first_single_meal_endpoint(self):
    #     meal_id = str(self.breakfast.id)
    #     response = self.client.get(f'/api/v1/meals/{meal_id}/foods')
    #
    #     meal_response = response.json()
    #
    #     self.assertEqual(meal_response['name'], 'Breakfast')
    #     self.assertEqual(meal_response['foods'][0]['name'], self.apple.name)
    #     self.assertEqual(meal_response['foods'][0]['calories'], self.apple.calories)
    #     self.assertEqual(meal_response['foods'][1]['name'], self.banana.name)
    #     self.assertEqual(meal_response['foods'][1]['calories'], self.banana.calories)
    #
    #
    # def test_sad_path_show_meal_endpoint(self):
    #     response = self.client.get('/api/v1/meals/99/foods')
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
