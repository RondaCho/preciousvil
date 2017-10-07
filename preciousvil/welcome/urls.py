from django.conf import settings
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='welcome'),
    url(r'^dashboard/$', views.dash_board, name='dash_board'),
]