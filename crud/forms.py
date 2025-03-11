from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student # This is where you specify the model
        fields = ('__all__')
