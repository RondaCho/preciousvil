#welcome/views.py
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.apps import apps
from .models import HeroImage, Reservation, Type
from .forms import ReservationForm,SecretForm

House1 = apps.get_model('dashboard','House')

house_list = House1.objects.all

def main_page(request):
    hero_image = HeroImage.objects.all

    return render(request, 'welcome/main_page.html', {
        'heroimage' : hero_image,
    })

def overview(request):
    return render(request,'welcome/overview.html')

def house_detail(request):
    return render(request, 'welcome/house_a.html', {
        'house_list': house_list,
    })
def house_a(request):
    return render(request, 'welcome/house_a.html',{
        'house_list':house_list,
    })
def house_b(request):
    return render(request, 'welcome/house_b.html', {
        'house_list':house_list,
    })
def house_c(request):
    return render(request, 'welcome/house_c.html', {
        'house_list':house_list,
    })
def house_d(request):
    return render(request, 'welcome/house_d.html', {
        'house_list':house_list,
    })


def architect(request):
    pass


def community_detail(request):
    return render(request, 'welcome/community_detail.html')


def environment_detail(request):
    return render(request, 'welcome/environment_detail.html')


def visit_us(request):
    return render(request, 'welcome/visit_us.html')

rsv_list = Reservation.objects.all

def reservation_new(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST, request.FILES) # 유저로 부터 받은 데이터를 폼에 넘겨받는다.
        if form.is_valid():
            reservation = form.save()
            return redirect('welcome:reservation') # urlreverse를 사용할 때에는 namespace:name 사용 가능.
    else:
        form = ReservationForm()
    return render(request, 'welcome/reservation_form.html', {
        'form': form,
    })

def reservation_list(request):
    return render(request, 'welcome/reservation.html', {
        'reservation_list' : rsv_list,
    })

def reservation_detail(request,id):
    reservation = get_object_or_404(Reservation, id=id)
    if request.method =='POST':
        form = SecretForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            phone_number = data['phone_number']
            if phone_number == reservation.phone_number:
                return render(request,'welcome/reservation_detail.html',{
                    'form':form,
                    'phone_number':phone_number,
                    'reservation':reservation,
                })
    else:
        form = SecretForm()
    return render(request, 'welcome/reservation_secret.html', {
        'form' : form,
        'reservation':reservation,
    })
'''
def reservation_detail(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    return render(request, 'welcome/reservation_detail.html', {
        'reservation' : reservation,
    })
'''

'''
def reservation_secret(request, id):
    secret_post = Reservation.objects.get(id=id)
    if request.method =='POST':
        form = SecretForm(request.POST)
        if form == secret_post.phone_number:
            return redirect('welcome:reservation_detail')
        else:
            messages.warning(request, '입력하신 전화번호와 같지 않습니다.')
    else:
        form = SecretForm()
    return render(request, 'welcome/reservation_secret.html', {
        'form': form,
    })
'''