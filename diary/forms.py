# forms.py
from django import forms
from .models import DiaryEntry

class DiaryEntryForm(forms.ModelForm):
    class Meta:
        model = DiaryEntry
        fields = '__all__'  # Or specify the fields you want to include in the form
