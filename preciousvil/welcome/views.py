#welcome/views.py
from django.shortcuts import render
from .models import Progress

def main_page(request):
    return render(request, 'welcome/main_page.html')

def dash_board(request):
    qs = Progress.objects.all()

    return render(request, 'welcome/dash_board.html', {
        'progress' : qs
    })