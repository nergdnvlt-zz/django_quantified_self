from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import FoodViews, MealViews, MealFoodViews

urlpatterns = {
    path('v1/foods/', FoodViews.as_view({'get': 'list',
                                         'post': 'create'})),
    path('v1/foods/<food_id>', FoodViews.as_view({'get': 'retrieve',
                                                  'put': 'update',
                                                  'patch': 'partial_update',
                                                  'delete': 'destroy'})),
    path('v1/meals/', MealViews.as_view({'get': 'list'})),
    path('v1/meals/<meal_id>/foods', MealViews.as_view({'get': 'retrieve'})),
    path('v1/meals/<meal_id>/foods/<food_id>', MealFoodViews.as_view({'post': 'create', 'delete': 'destroy'})),
}

urlpatterns = format_suffix_patterns(urlpatterns)
