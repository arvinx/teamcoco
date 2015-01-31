from django import forms

class SeniorForm(forms.Form):
    name = forms.CharField(label='name', max_length=40)
    phone_number = forms.CharField(label='phone_number')