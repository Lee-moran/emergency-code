from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_ngos, name='ngos'),
    path('<int:nongovernmentorg_id>/', views.ngo_detail, name='ngo_detail'),
]
