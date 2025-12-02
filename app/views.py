from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Coach, Player
from .forms import JoinRequestForm


def index(request):
    if request.method == 'POST':
        form = JoinRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Заявка успешно отправлена!")
            return redirect('index') 
    else:
        form = JoinRequestForm()
    return render(request, 'app/index.html', {'form': form})


def coach_cards(request):
    """Страница тренерского штаба"""
    coaches = Coach.objects.all()
    return render(request, 'app/coach_cards.html', {'coaches': coaches})


def player_cards(request):
    """Страница игроков"""
    players = Player.objects.all()
    return render(request, 'app/player_cards.html', {'players': players})