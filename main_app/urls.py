from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tickets/', views.tickets_index, name='index'),
    path('tickets/<int:ticket_id>/', views.tickets_detail, name='detail'),
    path('tickets/create/', views.TicketCreate.as_view(), name='tickets_create'),
    path('accounts/signup/', views.signup, name='signup'),
    path('tickets/<int:pk>/update/', views.TicketUpdate.as_view(), name='tickets_update'),
    path('tickets/<int:pk>/delete/', views.TicketDelete.as_view(), name='tickets_delete'),
    path('tickets/<int:ticket_id>/add_highlight/', views.add_highlight, name='add_highlight')
]