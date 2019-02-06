from django import forms
from .models import *


class EventForm(forms.ModelForm):

    class Meta:
        model = Evento
        exclude = ('created_date',)