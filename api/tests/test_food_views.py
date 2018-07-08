import json
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from api.models import Food

class FoodsEndpointTest(TestCase):
    def setUp(self):
        self.client=APIClient()
        Food.objects.create(name="apple", calories=100)
        Food.objects.create(name="delicious ramen", calories=888)
        Food.objects.create(name="banana", calories=100)

    def test_status_for_all_foods(self):
        response = self.client.get('/api/v1/foods/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_gets_all_foods(self):
        response = self.client.get('/api/v1/foods/').json()
        foods = Food.objects.all()
        self.assertEqual(len(response), 3)
        self.assertEqual(response[0]["name"], "apple")
        self.assertEqual(response[0]["calories"], 100)
        self.assertEqual(response[1]["name"], "delicious ramen")
        self.assertEqual(response[1]["calories"], 888)

    def test_gets_first_single_food_response(self):
        food = Food.objects.first()
        food_id = str(food.id)
        response = self.client.get(f'/api/v1/foods/{food_id}')
        food_response = response.json()
        self.assertEqual(food_response["name"], "apple")
        self.assertEqual(food_response["calories"], 100)

    def test_sad_path_show_food_response(self):
        food = Food.objects.first()
        response = self.client.get('/api/v1/foods/99')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_creates_new_food(self):
        response = self.client.post('/api/v1/foods/', {'food': {'name': 'OMG so good ramen', 'calories': 1888}}, format='json')
        food_response = response.json()
        self.assertEqual(food_response["name"], "OMG so good ramen")
        self.assertEqual(food_response["calories"], 1888)

    def test_sad_path_create_food_name(self):
        response = self.client.post('/api/v1/foods/', {'food': {'calories': 1888}}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_sad_path_create_food_calories(self):
        response = self.client.post('/api/v1/foods/', {'food': {'name': 'bad'}}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_updates_current_food(self):
        food = Food.objects.first()
        food_id = str(food.id)
        response = self.client.patch(f'/api/v1/foods/{food_id}', {'food': {'name': 'kiwi', 'calories': 68}}, format='json')
        food_response = response.json()
        self.assertEqual(food_response["name"], "kiwi")
        self.assertEqual(food_response["calories"], 68)

    def test_without_name_doesnt_update_food(self):
        food = Food.objects.first()
        food_id = str(food.id)
        response = self.client.patch(f'/api/v1/foods/{food_id}', {'food': {'calories': 68}}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_without_calories_doesnt_update_food(self):
        food = Food.objects.first()
        food_id = str(food.id)
        response = self.client.patch(f'/api/v1/foods/{food_id}', {'food': {'name': 'lemon'}}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_deletes_food(self):
        food = Food.objects.last()
        food_id = str(food.id)
        response = self.client.delete(f'/api/v1/foods/{food_id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_sad_path_for_deletes_food(self):
        response = self.client.delete(f'/api/v1/foods/101')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
