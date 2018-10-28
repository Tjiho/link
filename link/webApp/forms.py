from django import forms

class LinkForm(forms.Form):
    link = forms.CharField(label="add a link",widget=forms.TextInput(attrs={'placeholder': 'Paste your link'}))