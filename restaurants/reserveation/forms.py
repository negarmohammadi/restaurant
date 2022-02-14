from django import forms
from .models import reservation

class reservationForm(forms.ModelForm):
    class Meta:
        model = reservation
        fields = {"name","student_number","phone","Food_name", "number","date","time"}