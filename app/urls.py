from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('coaches/', views.coach_cards, name='coach_cards'),
    path('players/', views.player_cards, name='player_cards'),
]