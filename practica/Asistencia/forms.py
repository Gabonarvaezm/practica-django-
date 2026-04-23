from django import forms
from .models import Asistencia

class asistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = '__all__'