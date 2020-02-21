__author__ = 'sergeypunin'

from django.urls import path
from . import views

urlpatterns = [
#    path(r'', views.post_list, name='post_list'),
    path(r'', views.main, name='main'),
    path(r'test', views.test, name='test'),
    path(r'test-ajax', views.test_ajax, name='test_ajax'),
]