from django.forms import ModelForm
from .models import Highlight

class HighlightForm(ModelForm):
  class Meta:
    model = Highlight
    fields = ['content', 'video_url']