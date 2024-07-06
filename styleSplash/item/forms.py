from django import forms
from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')

        widgets = {
            'category':forms.Select(attrs={
                'class':''
            }),
            'name':forms.TextInput(attrs={
                'class':''
            }),
            'description':forms.Textarea(attrs={
                'class':''
            }),
            'price':forms.TextInput(attrs={
                'class':''
            }),
            'image':forms.FileInput(attrs={
                'class':''
            })
        }

