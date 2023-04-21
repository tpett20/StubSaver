from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


EVENT_TYPES = (
    ('C', 'Concert'),
    ('S', 'Sport'),
)

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    maps_url = models.URLField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('location_detail', kwargs={'pk': self.id})
    
    class Meta: 
        ordering = ['name']


class Ticket(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField('date (yyyy-mm-dd)')
    companion = models.CharField(max_length=250)
    event_type = models.CharField(max_length=1, choices=EVENT_TYPES, default=EVENT_TYPES[0][0])
    artists = models.ManyToManyField(Artist, blank=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} on {self.date}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'ticket_id': self.id})
    
    class Meta: 
        ordering = ['-date']


class SportEvent(models.Model):
    sport = models.CharField(max_length=100)
    league = models.CharField(max_length=100)
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    home_score = models.IntegerField()
    away_score = models.IntegerField()
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.home_team} v. {self.away_team}"


class Highlight(models.Model):
    content = models.TextField('Your Highlights')
    video_url = models.CharField(null=True, blank=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    def __str__(self):
        return self.content