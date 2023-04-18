from django.shortcuts import render

tickets = [
    {
    'name': 'yankees vs mets', 'sport': 'Baseball'
    }
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def tickets_index(request):
    return render(request, 'tickets/index.html', {
        'tickets': tickets
    })