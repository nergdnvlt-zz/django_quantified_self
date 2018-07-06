from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import FoodViews

urlpatterns = {
    url(r'^foods', FoodViews.as_view({'get': 'list', 'post': 'create'})),
    url(r'^foods/(?P<food_id>\d+)', FoodViews.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}))
}

urlpatterns = format_suffix_patterns(urlpatterns)
