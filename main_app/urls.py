from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tickets/', views.tickets_index, name='index'),
    path('tickets/<int:ticket_id>/', views.tickets_detail, name='detail'),
]