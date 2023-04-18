from django.shortcuts import render
from .models import Ticket

# Create your views here.
def home(request):
    return render(request, 'home.html')

def tickets_index(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/index.html', {
        'tickets': tickets
    })