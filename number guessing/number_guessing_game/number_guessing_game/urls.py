from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('guessing_game.urls')),  # Add this line to include guessing_game URLs
]
