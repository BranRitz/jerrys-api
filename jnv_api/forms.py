from django import forms

class AttemptForm(forms.Form):
    word = forms.CharField()


