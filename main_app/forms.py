from django.forms import ModelForm
from .models import Highlight, Artist

class HighlightForm(ModelForm):
    class Meta:
        model = Highlight
        fields = ['content', 'video_url']

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = ['name']