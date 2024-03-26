from django.urls import path
from .views import home, calc_view, calculate_view  # Import the views

urlpatterns = [
    path('', home, name='home'),  # URL pattern for the home page
    path('calculator/', calc_view, name='calculator'), # URL pattern for the calculator page
    path('calculate', calculate_view, name='calculate'),  # URL pattern for the calculation logic
]
