from django import forms
from .models import person


class personform(forms.ModelForm):
    fields=('name','age','email','address',)
    model=person
