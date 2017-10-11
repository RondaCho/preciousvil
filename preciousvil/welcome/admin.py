# welcome/admin.py

from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import HeroImage

@admin.register(HeroImage)
class HeroImageAdmin(admin.ModelAdmin):
    list_display = ['name','photo']