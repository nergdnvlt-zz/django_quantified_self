from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()

class Meal(models.Model):
    name = models.CharField(max_length=100)
    foods = models.ManyToManyField(Food)
