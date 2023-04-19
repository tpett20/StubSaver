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

class Ticket(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField('date (yyyy-mm-dd)')
    companion = models.CharField(max_length=250)
    event_type = models.CharField(max_length=1, choices=EVENT_TYPES, default=EVENT_TYPES[0][0])
    artists = models.ManyToManyField(Artist)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'ticket_id': self.id})

class Highlight(models.Model):
    content = models.TextField('Your Highlights')
    video_url = models.CharField(null=True, blank=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    def __str__(self):
        return self.content