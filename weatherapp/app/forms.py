from django import forms

class cityForm(forms.Form):
    name = forms.CharField(max_length=30, label="City")