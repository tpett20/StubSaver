from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ticket, Artist, Location
from .forms import HighlightForm, ArtistForm, SportEventForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

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
    artist_form = ArtistForm()
    sportevent_form = SportEventForm()
    return render(request, 'tickets/detail.html', {
        'ticket': ticket,
        'highlight_form': highlight_form,
        'artists': unassociated_artists, 
        'artist_form': artist_form,
        'sportevent_form': sportevent_form
    })

@login_required
def add_highlight(request, ticket_id):
    form = HighlightForm(request.POST)
    if form.is_valid():
        new_highlight = form.save(commit=False)
        new_highlight.ticket_id = ticket_id
        new_highlight.save()
    return redirect('detail', ticket_id=ticket_id)

@login_required
def add_artist(request, ticket_id):
    form = ArtistForm(request.POST)
    if form.is_valid():
        new_artist = form.save()
        new_artist.save()
    return redirect('detail', ticket_id=ticket_id)

@login_required
def add_sportevent(request, ticket_id):
    form = SportEventForm(request.POST)
    if form.is_valid():
        new_sportevent = form.save(commit=False)
        new_sportevent.ticket_id = ticket_id
        new_sportevent.user = request.user
        new_sportevent.save()
    return redirect('detail', ticket_id=ticket_id)

@login_required
def assoc_artist(request, ticket_id, artist_id):
    Ticket.objects.get(id=ticket_id).artists.add(artist_id)
    return redirect('detail', ticket_id=ticket_id)

@login_required
def unassoc_artist(request, ticket_id, artist_id):
    Ticket.objects.get(id=ticket_id).artists.remove(artist_id)
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

class TicketCreate(LoginRequiredMixin, CreateView):
    model = Ticket
    fields = ['name', 'date', 'location', 'companion', 'event_type']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class TicketUpdate(LoginRequiredMixin, UpdateView):
    model = Ticket
    fields = ['name', 'date', 'location', 'companion', 'event_type']

class TicketDelete(LoginRequiredMixin, DeleteView):
    model = Ticket
    success_url = '/tickets'

class LocationIndex(LoginRequiredMixin, ListView):
    model = Location

    # https://stackoverflow.com/questions/24725617/how-to-make-generic-listview-only-show-users-listing
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

class LocationDetail(LoginRequiredMixin, DetailView):
    model = Location

class LocationCreate(LoginRequiredMixin, CreateView):
    model = Location
    fields = ['name', 'city', 'country', 'maps_url']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)