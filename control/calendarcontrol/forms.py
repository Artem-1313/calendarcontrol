from django import forms
from django.forms import ModelForm

from .models import telegramsControl

class ModalForm(ModelForm):
    class Meta:
        model = telegramsControl
        fields = ('date', 'unit_to_report','tlg_number','description','priority','tlg_scan')
