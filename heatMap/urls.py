from django.urls import path
from .views import heatMap

urlpatterns = [
    path('', heatMap),
]
