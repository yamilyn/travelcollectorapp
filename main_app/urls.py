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
    path('travels/<int:travel_id>/add_checking/', views.add_checking, name='add_checking'),
    
    # Status Model
    path('status/', views.StatusList.as_view(), name = 'status_index'),
    path('status/<int:pk>/', views.StatusDetail.as_view(), name='status_detail'),
    path('status/create/', views.StatusCreate.as_view(), name='status_create'),
    path('status/<int:pk>/update/', views.StatusUpdate.as_view(), name='status_update'),
    path('status/<int:pk>/delete/', views.StatusDelete.as_view(), name='status_delete'),

    # M:M
    path('travels/<int:travel_id>/assoc_status/<int:status_id>/', views.assoc_status, name='assoc_status'),
    path('travels/<int:travel_id>/unassoc_status/<int:status_id>/', views.unassoc_status, name='unassoc_status'),
]