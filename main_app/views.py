from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ticket, Artist
from .forms import HighlightForm

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
    id_list = ticket.artists.all().values_list('id')
    unassociated_artists = Artist.objects.exclude(id__in=id_list)
    highlight_form = HighlightForm()
    return render(request, 'tickets/detail.html', {
        'ticket': ticket,
        'highlight_form': highlight_form,
        'artists': unassociated_artists 
    })

def add_highlight(request, ticket_id):
    form = HighlightForm(request.POST)
    if form.is_valid():
        new_highlight = form.save(commit=False)
        new_highlight.ticket_id = ticket_id
        new_highlight.save()
    return redirect('detail', ticket_id=ticket_id)

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

class TicketCreate(CreateView):
    model = Ticket
    fields = ['name', 'date', 'companion', 'event_type']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class TicketUpdate(UpdateView):
    model = Ticket
    fields = ['name', 'date', 'companion', 'event_type']

class TicketDelete(DeleteView):
    model = Ticket
    success_url = '/tickets'
