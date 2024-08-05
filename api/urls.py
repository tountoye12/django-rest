
from django.urls import path

from . import views


urlPatters = [
    path('', views.getData),
]