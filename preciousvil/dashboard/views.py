from django.shortcuts import render
from .models import Progress, House

def dash_board(request):
    progress_list = Progress.objects.all()
    house_list = House.objects.all()

    return render(request, 'dashboard/dash_board.html', {
        'progress_list' : progress_list,
        'house_list': house_list
    })
