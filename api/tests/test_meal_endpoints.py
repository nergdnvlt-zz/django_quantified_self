import json
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from api.models import Food, Meal

class MealsEndpointTest(TestCase):

    def setUp(self):
        self.client=APIClient()
        self.apple = Food.objects.create(name="apple", calories=100)
        self.ramen = Food.objects.create(name="delicious ramen", calories=888)
        self.banana = Food.objects.create(name="banana", calories=99)
        self.dessert = Food.objects.create(name="dessert", calories=1000)

        self.breakfast = Meal.objects.create(name="Breakfast")
        self.snack = Meal.objects.create(name="Snack")

        self.breakfast.foods.add(self.apple)
        self.breakfast.foods.add(self.banana)

        self.snack.foods.add(self.ramen)
        self.snack.foods.add(self.dessert)


    def test_status_for_all_meals(self):
        response = self.client.get('/api/v1/meals/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_gets_all_meals(self):
        response = self.client.get('/api/v1/meals/').json()
        meals = Meal.objects.all()

        self.assertEqual(len(response), 2)

        self.assertEqual(response[0]['name'], self.breakfast.name)
        self.assertEqual(len(response[0]['foods']), 2)
        self.assertEqual(response[0]['foods'][0]['name'], self.apple.name)
        self.assertEqual(response[0]['foods'][0]['calories'], self.apple.calories)
        self.assertEqual(response[0]['foods'][1]['name'], self.banana.name)
        self.assertEqual(response[0]['foods'][1]['calories'], self.banana.calories)

        self.assertEqual(response[1]['name'], self.snack.name)
        self.assertEqual(len(response[1]['foods']), 2)
        self.assertEqual(response[1]['foods'][0]['name'], self.ramen.name)
        self.assertEqual(response[1]['foods'][0]['calories'], self.ramen.calories)
        self.assertEqual(response[1]['foods'][1]['name'], self.dessert.name)
        self.assertEqual(response[1]['foods'][1]['calories'], self.dessert.calories)



    def test_gets_first_single_meal_endpoint(self):
        meal_id = str(self.breakfast.id)
        response = self.client.get(f'/api/v1/meals/{meal_id}/foods')

        meal_response = response.json()

        self.assertEqual(meal_response['name'], 'Breakfast')
        self.assertEqual(meal_response['foods'][0]['name'], self.apple.name)
        self.assertEqual(meal_response['foods'][0]['calories'], self.apple.calories)
        self.assertEqual(meal_response['foods'][1]['name'], self.banana.name)
        self.assertEqual(meal_response['foods'][1]['calories'], self.banana.calories)


    def test_sad_path_show_meal_endpoint(self):
        response = self.client.get('/api/v1/meals/99/foods')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
