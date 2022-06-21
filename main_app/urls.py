from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('travels/', views.travels_index, name='index'),
    path('travels/<int:travel>/', views.travels_detail, name='detail')
]