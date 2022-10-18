from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


ACCT_CHOICES = [('professor', 'Professor'), ('student', 'Student')]

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    account_type = forms.ChoiceField(choices=ACCT_CHOICES, widget=forms.RadioSelect)
    # account_type = forms.CharField(label='Account Type:', widget=forms.RadioSelect(attrs={'class': "custom-radio-list"},
    #                                                                      choices=ACCT_CHOICES))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'account_type')

