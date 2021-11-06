from django import forms
from django.forms import fields
from .models import DataCenter

class DataCenterForm(forms.ModelForm):

    class Meta:
        model = DataCenter
        fields = ('titulo', 'descricao', 'sustentavel', 'preco', 'categoria', 'setor', 'consumo_eletrico')