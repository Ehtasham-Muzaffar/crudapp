from django import forms
from django.db.models import fields
from django.forms import widgets
from curdapp.models import user


class Userform(forms.ModelForm):
    class Meta:
        model=user
        fields="__all__"
        widgets={
            'uname':forms.TextInput(attrs={'class':'form-control'}),
            'uEmail':forms.EmailInput(attrs={'class':'form-control'}),
            'uPassword':forms.PasswordInput(attrs={'class':'form-control'})
        }