from .models import Super
from django import forms

class SuperForm(forms.ModelForm):
    class Meta:
        model = Super
        fields = '__all__'