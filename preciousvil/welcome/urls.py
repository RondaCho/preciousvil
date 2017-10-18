from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='welcome'),

    url(r'^overview/$', views.overview, name='overview'),

    url(r'^house/$', views.house_a, name='house'),
    url(r'^house/atype',views.house_a, name='house_a'),
    url(r'^house/btype',views.house_b, name='house_b'),
    url(r'^house/ctype', views.house_c, name='house_c'),
    url(r'^house/dtype', views.house_d, name='house_d'),

    url(r'^architect/$', views.architect, name='architect'),

    url(r'^community/$', views.community_detail, name='community'),

    url(r'^environment/$', views.environment_detail, name='environment'),

    url(r'^visitus/$', views.visit_us, name='visitus'),
    url(r'^reservation/$', views.reservation_list, name='reservation'),
    url(r'^reservation/new/$', views.reservation_new, name='reservation_new'),
    url(r'^reservation/(?P<id>\d+)/$', views.reservation_detail, name='reservation_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)