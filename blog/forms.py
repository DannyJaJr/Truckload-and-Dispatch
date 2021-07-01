from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    pwd = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    pwd = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    pwd_confirm = forms.CharField(label="Comfirm Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))





