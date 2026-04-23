from django import forms
from .models import Reporte

class reporteForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = '__all__'