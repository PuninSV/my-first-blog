__author__ = 'sergeypunin'

from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.post_list, name='post_list'),
]