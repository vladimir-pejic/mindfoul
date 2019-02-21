from django.urls import path
from .views import index, CityDeleteView



urlpatterns = [
    path('', index, name='weather'),
    path('/<int:pk>/delete', CityDeleteView.as_view(), name='weather.delete'),
]