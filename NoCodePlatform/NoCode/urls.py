from django.urls import path


from .views import *

urlpatterns = [
    path('', index),
    path('tests', ThirdDimension),
    path('report', report),
]

