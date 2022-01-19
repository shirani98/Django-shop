from django import forms

class AddToCardForm(forms.Form):
    number = forms.IntegerField(min_value=1, max_value=9 , label="" ,widget=forms.NumberInput(attrs={'class': 'form-control text-center me-3', 'type': 'number', 'style' : 'max-width: 5rem', 'id' : 'inputQuantity', 'value' : '1','min' : '1','max' : '9', }))