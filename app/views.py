from django.shortcuts import render
from .models import Coach

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def coach_cards(request):
    """Страница тренерского штаба"""
    coaches = Coach.objects.all()
    return render(request, 'app/coach_cards.html', {'coaches': coaches})
