__author__ = 'sergeypunin'

from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.calc, name='calc'),
    path(r'ajax', views.ajax, name='ajax'),
    path(r'water', views.water, name='water'),
    path(r'calc.js', views.calc_js, name='calc_js'),
]
