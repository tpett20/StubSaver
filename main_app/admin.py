from django.contrib import admin
from .models import Artist, Ticket, Highlight, Location

# Register your models here.
admin.site.register(Artist)
admin.site.register(Ticket)
admin.site.register(Highlight)
admin.site.register(Location)