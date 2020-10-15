from .models import Soru,Cevaplar
from django.forms import ModelForm
from django import forms

class SoruForm(ModelForm):
    class Meta:
        model = Soru
        fields = ['soran','sorukonu', 'soru', 'image']
        labels = {
            'soran': ('Soruyu Soran'),
            'sorukonu': ('Soru Konusu'),
            'soru': ('Sorunuz'),
            'image': ('Soru ile İlgili Resim'),
        }

        widgets = {
            "soran" : forms.TextInput(attrs={'size': 20, 'class': 'form-control','placeholder':"Lütfen Adınızı Girin.."}),
            "soru" : forms.Textarea(attrs={'size': 20, 'class': 'form-control','placeholder':"Lütfen Sorunuzu Girin.."}),
            "image" : forms.FileInput(attrs={'size': 20, 'class': 'form-control-file'}),
        }


class CevapForm(ModelForm):
    class Meta:
        model = Cevaplar
        fields = ['cevaplayan', 'cevap', 'image']
        labels = {
            'cevaplayan': ('Cevaplayan'),
            'cevap': ('Soru ile ilgili Cevabınız'),
            'image': ('Cevabınız ile İlgili Resim'),
        }

        widgets = {
            "cevaplayan" : forms.TextInput(attrs={'size': 20, 'class': 'form-control','placeholder':"Lütfen Adınızı Girin.."}),
            "cevap" : forms.Textarea(attrs={'size': 20, 'class': 'form-control','placeholder':"Lütfen Sorunuzu Girin.."}),
            "image" : forms.FileInput(attrs={'size': 20, 'class': 'form-control-file'}),
        }
