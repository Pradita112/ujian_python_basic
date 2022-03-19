from django import forms

class AddMakananform(forms.Form):
    nama = forms.CharField(max_length=45, label='nama_makanan', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    asal = forms.CharField(max_length=45, label='asal_makanan', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    gambar = forms.ImageField(label= 'gambar',widget=forms.FileInput(attrs={
        'class':"form-control",
    }))
class EditMakananForm(forms.Form):
    nama = forms.CharField(max_length=15, label = "Nama", widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    asal = forms.CharField(max_length=15, label = "asal_makanan", widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    gambar = forms.ImageField(required=False,label = "Gambar")