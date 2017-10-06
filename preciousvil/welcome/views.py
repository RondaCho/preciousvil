#welcome/views.py
from django.shortcuts import render

def main_page(request):
    return render(request, 'welcome/main_page.html')