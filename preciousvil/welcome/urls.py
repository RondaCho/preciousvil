from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='welcome'),
    url(r'^overview/$', views.overview, name='overview'),
    url(r'^house/$', views.house_detail, name='house'),
    url(r'^house/atype',views.house_detail, name='house_a'),
    url(r'^house/btype',views.house_detail, name='house_b'),
    url(r'^house/ctype', views.house_detail, name='house_c'),
    url(r'^house/dtype', views.house_detail, name='house_d'),
    url(r'^community/$', views.community_detail, name='community'),
    url(r'^environment/$', views.environment_detail, name='environment'),
    url(r'^visitus/$', views.visit_us, name='visitus'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)