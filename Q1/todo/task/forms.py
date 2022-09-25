from ast import Sub
from django import forms
from .models import tasks

class taskForms(forms.ModelForm):
    class Meta:
        model = tasks
        fields = '__all__'