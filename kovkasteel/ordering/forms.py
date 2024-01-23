from django import forms
from .models import *
from django.forms import TextInput, Textarea


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'phone', 'email', 'message', 'photo']

        widgets = {
            'name':TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Имя',
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон'
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'message': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание проекта'
            })
        }