from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('travels/', views.travels_index, name='index'),
    path('travels/<int:travel_id>/', views.travels_detail, name='detail'),
    path('travels/create/', views.TravelCreate.as_view(), name='travels_create'),
    path('travels/<int:pk>/update/', views.TravelUpdate.as_view(), name='travels_update'),
    path('travels/<int:pk>/delete/', views.TravelDelete.as_view(), name='travels_delete'),
]