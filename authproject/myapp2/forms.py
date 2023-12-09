from django import forms
from .models import*

class si(forms.ModelForm):
    class Meta:
        model=peoplesign
        fields='__all__'