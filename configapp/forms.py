import re

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from pydantic import ValidationError

from .models import *

class NewForm(forms.Form):
    title=forms.CharField(max_length=150, label='Malumot',
                          widget=forms.TextInput(attrs={"class": "form-control"}))
    context=forms.CharField(label='Teks',required=False,widget=forms.Textarea(attrs={
        "class":"form-control",
        "rows":5
    }))
    is_bool=forms.BooleanField(label='malumot?',initial=True)
    category=forms.ModelChoiceField(empty_label='Category tanlang',
                                    label='Category',queryset=Category.objects.all(),
                                    widget=forms.Select(attrs={"class": "form-control"}))

class CategoryForm(forms.Form):
    title = forms.CharField(max_length=150, label='Malumot',
                            widget=forms.TextInput(attrs={"class": "form-control"}))


class NewsForm(forms.ModelForm):
    class Meta:
        model=News
        fields=['title','context','is_bool','category']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'context':forms.Textarea(attrs={'class':'form-control','row':5}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }

    def clean_title(self):
        title=self.cleaned_data['title']
        if re.match(r'\d',title):
            raise ValidationError('Title raqam bulmasin')
        return title

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='login',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))


    class Meta:
        model=User
        fields=('username','password',)