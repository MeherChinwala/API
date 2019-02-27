from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('list', views.TrackView)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^create/$', views.TrackCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.TrackRetrieve.as_view(), name = 'retrieve'),
    url(r'^(?P<pk>\d+)/edit/$', views.TrackUpdate.as_view(), name = 'update'),
    url(r'^(?P<pk>\d+)/delete/$', views.TrackDelete.as_view(), name = 'delete'),

]