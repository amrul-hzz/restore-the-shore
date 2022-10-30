from django import forms

class AccountForm(forms.Form):
    username = forms.CharField(required=False,
                    widget=forms.TextInput(attrs={'placeholder': 'Cari Nama'}))
