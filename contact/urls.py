# -*- coding: utf-8 -*-
"""
@author: dan.wlodarski
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
