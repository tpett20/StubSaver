from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Ticket

# Create your views here.
def home(request):
    title = 'StubSaver'
    return render(request, 'home.html', {
        'title': title
    })

@login_required
def tickets_index(request):
    tickets = Ticket.objects.filter(user=request.user)
    return render(request, 'tickets/index.html', {
        'tickets': tickets
    })

@login_required
def tickets_detail(request, ticket_id):
    tickets = Ticket.objects.filter(user=request.user)
    ticket = tickets.get(id=ticket_id)
    return render(request, 'tickets/detail.html', {
        'ticket': ticket
    })

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)