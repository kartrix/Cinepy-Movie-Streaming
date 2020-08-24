from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('action/', views.action, name="action"),
    path('comedy/', views.comedy, name="comedy"),
    path('drama/', views.drama, name="drama"),
    path('fantasy/', views.fantasy, name="fantasy"),
    path('oscars/', views.oscars, name="oscars"),
    path('popular/', views.popular, name="popular"),
    path('romance/', views.romance, name="romance"),
    path('thriller/', views.thriller, name="thriller"),
    path('top/', views.top, name="top"),

]
