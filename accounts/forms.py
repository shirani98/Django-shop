from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label= "Password", widget= forms.PasswordInput)
    password2 = forms.CharField(label= "Password confirmation", widget= forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email', 'phone']
        
    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2 and password1 and password2:
            raise ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        
        
    
    