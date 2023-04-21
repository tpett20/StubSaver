from django.forms import ModelForm
from .models import Highlight, Artist, SportEvent

class HighlightForm(ModelForm):
    class Meta:
        model = Highlight
        fields = ['content', 'video_url']

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = ['name']

class SportEventForm(ModelForm):
    class Meta:
        model = SportEvent
        fields = ['sport', 'league', 'home_team', 'away_team', 'home_score', 'away_score']