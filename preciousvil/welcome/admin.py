# welcome/admin.py

from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import HeroImage, Reservation, Type

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    actions = ['v_reservation', 's_reservation','completed']
    list_display = ['name', 'phone_number','email', 'address', 'date', 'updated_at', 'status']

    def v_reservation(self, request, queryset):
        updated_count = queryset.update(status='v')
        self.message_user(request, '{} 건의 문의가 찾아가는 분양상담으로 변경됩니다.'.format(updated_count))
    v_reservation.short_description = '찾아가는 분양상담으로 상태변경'

    def s_reservation(self, request, queryset):
        updated_count = queryset.update(status='v')
        self.message_user(request, '{} 건의 문의가 현장방문 상담예약으로 변경됩니다.'.format(updated_count))
    s_reservation.short_description = '현장방문 분양상담으로 상태변경'

    def completed(self, request, queryset):
        updated_count = queryset.update(status='c')
        self.message_user(request, '{} 건의 문의가 상담완료 상태로 변경됩니다.'.format(updated_count))
    completed.short_description = '상담완료로 상태변경.'


@admin.register(HeroImage)
class HeroImageAdmin(admin.ModelAdmin):
    list_display = ['name','photo']

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['name']