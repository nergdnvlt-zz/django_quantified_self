from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import FoodViews

urlpatterns = {
    path('v1/foods/', FoodViews.as_view({'get': 'list',
                                         'post': 'create'})),
    path('v1/foods/<food_id>', FoodViews.as_view({'get': 'retrieve',
                                                  'put': 'update',
                                                  'patch': 'partial_update',
                                                  'delete': 'destroy'}))
}

urlpatterns = format_suffix_patterns(urlpatterns)
