from django.forms import ModelForm
from .models import Checking

class CheckingForm(ModelForm):
    class Meta:
        model = Checking
        fields = ['date']