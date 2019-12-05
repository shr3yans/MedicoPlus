from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('^$', views.post_list, name='post_list'),
    url(r'^mp$',views.mp,name='mp'),
    url(r'^find_doctor$',views.fd,name='fd'),
    url(r'^my_bookings$',views.mb,name='mb'),
    url(r'^book_appointment$',views.ba,name='ba'),
    url(r'^all_appointment$', views.alll, name='alll'),
]