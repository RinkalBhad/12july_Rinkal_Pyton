from django import forms
from.models import*

class sign(forms.ModelForm):
    class Meta:
        model=usersignup
        fields='__all__'
       # fields=['fistname','lastname','username','password','city','state','number']