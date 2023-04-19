from django.forms import ModelForm, TextInput, DateInput, NumberInput
from .models import Resident


class ResidentForm(ModelForm):
    class Meta:
        model = Resident
        fields =  '__all__'
        widgets = {
            'birthday': DateInput(attrs={'type': 'date'}),
            'admission_date': DateInput(attrs={'type': 'date'}),
            'discharge_date': DateInput(attrs={'type': 'date'}),
        }
    
