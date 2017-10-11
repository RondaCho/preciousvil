#welcome/views.py
from django.shortcuts import render
from .models import HeroImage

def main_page(request):
    hero_image = HeroImage.objects.all

    return render(request, 'welcome/main_page.html', {
        'heroimage' : hero_image,
    })

def overview(request):
    return render(request,'welcome/overview.html')

def house_detail(request):
    return render(request, 'welcome/house_detail.html')

def community_detail(request):
    return render(request, 'welcome/community_detail.html')

def environment_detail(request):
    return render(request, 'welcome/environment_detail.html')

def visit_us(request):
    return render(request, 'welcome/visit_us.html')
