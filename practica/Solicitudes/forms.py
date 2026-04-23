from django import forms
from .models import Solicitud


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['titulo', 'descripcion', 'estado', 'prioridad', 'archivo']

        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el título'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe tu solicitud',
                'rows': 4
            }),
            'estado': forms.Select(attrs={
                'class': 'form-select'
            }),
            'prioridad': forms.Select(attrs={
                'class': 'form-select'
            }),
            'archivo': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }

        labels = {
            'titulo': 'Título',
            'descripcion': 'Descripción',
            'estado': 'Estado',
            'prioridad': 'Prioridad',
            'archivo': 'Archivo (opcional)',
        }