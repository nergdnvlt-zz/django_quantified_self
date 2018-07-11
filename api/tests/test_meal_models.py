from django.test import TestCase

from api.models import Food, Meal

# Create your tests here.
class MealModelTestCase(TestCase):

    def setUp(self):
        self.apple = Food.objects.create(name="apple", calories=88)
        self.banana = Food.objects.create(name="banan", calories=108)
        self.cherry = Food.objects.create(name="cherry", calories=38)


    def test_meal_saves_to_db(self):
        breakfast = Meal.objects.create(name="Breakfast")

        count = Meal.objects.count()

        self.assertEqual(breakfast.name, "Breakfast")
        self.assertEqual(count, 1)


    def test_additional_meal_saves(self):
        breakfast = Meal.objects.create(name="Breakfast")
        first_count = Meal.objects.count()

        snack = Meal.objects.create(name="Snack")
        second_count = Meal.objects.count()

        self.assertEqual(snack.name, "Snack")
        self.assertEqual(first_count, 1)
        self.assertEqual(second_count, 2)


    def test_add_foods_to_meals(self):
        breakfast = Meal.objects.create(name="Breakfast")

        breakfast.foods.add(self.apple)
        self.assertEqual(len(breakfast.foods.all()), 1)

        breakfast.foods.add(self.banana)
        self.assertEqual(len(breakfast.foods.all()), 2)

        breakfast.foods.add(self.cherry)
        self.assertEqual(len(breakfast.foods.all()), 3)
