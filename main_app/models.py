from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


EVENT_TYPES = (
    ('C', 'Concert'),
    ('S', 'Sport'),
)

# Create your models here.
class Ticket(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    companion = models.CharField(max_length=250)
    event_type = models.CharField(max_length=1, choices=EVENT_TYPES, default=EVENT_TYPES[0][0])
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'ticket_id': self.id})
