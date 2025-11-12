from django.shortcuts import render
from .models import Coach, Player

# Create your views here.


def index(request):
    return render(request, 'app/index.html')


def coach_cards(request):
    """Страница тренерского штаба"""
    coaches = Coach.objects.all()
    return render(request, 'app/coach_cards.html', {'coaches': coaches})


def player_cards(request):
    """Страница игроков"""
    players = Player.objects.all()
    return render(request, 'app/player_cards.html', {'players': players})
