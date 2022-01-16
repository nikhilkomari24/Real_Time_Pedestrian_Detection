from django.urls import path,include
from authapi import views
import django_eventstream
from django.conf.urls import url, include

urlpatterns = [
    path('', include('djoser.urls')),
    path('',include('djoser.urls.authtoken')),
    path('restricted/',views.restricted,name='restricted'),
    url(r'^events/', include(django_eventstream.urls), {'channels': ['test']}),
    path('stream/',views.stream,name='stream'),

]
