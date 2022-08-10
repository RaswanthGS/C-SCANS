from django import forms
from django.forms import ModelForm, widgets
from .models import Contact

class PostForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs = {'class':'form-group form-control', 'style':'border: 2px solid black; width:120%',}),
            'email' : forms.EmailInput(attrs = {'class':'form-group form-control', 'style':'border: 2px solid black; width:120%'}),
            'subject' : forms.TextInput(attrs = {'class':'form-group form-control', 'style':'border: 2px solid black; width:120%'}),
            'message' : forms.Textarea(attrs = {'class':'form-group form-control', 'rows':3, 'style':'border: 2px solid black; width:120%'}),
        }