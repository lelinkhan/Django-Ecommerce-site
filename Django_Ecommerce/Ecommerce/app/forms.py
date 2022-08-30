from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from . models import Customer


class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Enter Username', min_length=3, max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Enter email', required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Enter Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = UsernameField(label='Enter Username',
                             widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': True}))
    password = forms.CharField(label='Enter Password', strip=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'autocomplete': 'current-password'}))


class MyChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', strip=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'autocomplete': 'current-password', 'autofocus': True}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'autocomplete': 'new-password'}),
                                    help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label='New Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'autocomplete': 'new-password'}))


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Enter Email', max_length=254, widget=forms.EmailInput(attrs={'class':'form-control','autocomplete':'email'}))


class MyPasswordSetForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'autocomplete': 'new-password'}),
                                    help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'autocomplete': 'new-password'}))



class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','locality','division','district','zipcode']

        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),
                   'locality':forms.TextInput(attrs={'class':'form-control'}),
                   'division':forms.TextInput(attrs={'class':'form-control'}),
                   'district':forms.Select(attrs={'class':'form-control'}),
                   'zipcode':forms.NumberInput(attrs={'class':'form-control'})
                   }