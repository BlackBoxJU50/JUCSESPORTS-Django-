from django import forms
from .models import InventoryItem

class InventoryForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['name', 'quantity', 'status', 'sport']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input border border-indigo-300 rounded-lg p-3 focus:ring-2 focus:ring-indigo-400',
                'placeholder': 'Item Name'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-input border border-indigo-300 rounded-lg p-3 focus:ring-2 focus:ring-indigo-400',
                'placeholder': 'Quantity'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select border border-indigo-300 rounded-lg p-3 focus:ring-2 focus:ring-indigo-400',
            }),
            'sport': forms.Select(attrs={
                'class': 'form-select border border-indigo-300 rounded-lg p-3 focus:ring-2 focus:ring-indigo-400',
            }),
        }
