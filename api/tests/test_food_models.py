from django.test import TestCase

from api.models import Food

# Create your tests here.
class FoodModelTestCase(TestCase):

    def test_food_saves_to_db(self):
        Food.objects.create(name="apple", calories=88)
        apple = Food.objects.get(name="apple")
        count = Food.objects.count()
        self.assertEqual(apple.name, "apple")
        self.assertEqual(apple.calories, 88)
        self.assertEqual(count, 1)

    def test_additional_food_saves(self):
        Food.objects.create(name="apple", calories=88)
        first_count = Food.objects.count()
        Food.objects.create(name="banana", calories=98)
        second_count = Food.objects.count()
        banana = Food.objects.last()
        self.assertEqual(banana.name, "banana")
        self.assertEqual(banana.calories, 98)
        self.assertEqual(first_count, 1)
        self.assertEqual(second_count, 2)
