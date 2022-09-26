import imp
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home),
    path('aboutoo/',views.About,name='aboutus'),
    path('dj/', views.Django)
]