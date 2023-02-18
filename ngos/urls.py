from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_ngos, name='ngos'),
    path('causes/', views.all_causes, name='all_causes'),
    path('cause_detail/<category_id>', views.cause_detail,
         name='cause_detail'),
]
