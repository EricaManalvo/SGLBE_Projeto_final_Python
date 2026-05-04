from django import forms
from .models import Lata

class LataForm(forms.ModelForm):

    class Meta:
        model = Lata
        fields = '__all__'