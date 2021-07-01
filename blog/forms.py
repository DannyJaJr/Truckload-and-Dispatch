from django import forms
from .models import Load


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    pwd = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    pwd = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    pwd_confirm = forms.CharField(label="Comfirm Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))


# class to rende for for CRUD
# (forms.ModelForm) heritance may from => froms.Form or forms.ModelForm
class LoadForm(forms.ModelForm):
    class Meta:
        model = Load
        fields = ['title', 'category','price', 'desc', 'image']
        labels = {'title': 'Title', 'category': 'Category', 'price': 'Price', 'desc': 'Description'}
        # widget to install the bootstrap fomr control
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control', 'row':5}),
        }

