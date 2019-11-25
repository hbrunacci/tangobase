from django import forms
from .models import *


class CirugiaForm(forms.ModelForm):

    class Meta:
        model = Cirugia
        exclude = ('created_date',)