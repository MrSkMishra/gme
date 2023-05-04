from django.urls import path
from .views import *

urlpatterns = [
    path('games/', PalindromeGameListCreateAPIView.as_view(), name='game_list_create'),
    path('games/<int:pk>/', PalindromeGameRetrieveUpdateDeleteAPIView.as_view(), name='game_retrieve_update_destroy'),
]
