from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AttemptForm(forms.Form):
    word = forms.CharField()
    audio = forms.FileInput()


CATEGORY_CHOICES = [
    ('people', 'My Friends and Family'),
    ('outdoors', 'The Great Outdoors'),
    ('food', 'Restaurants and Food'),
    ('me', 'Me, Myself and I'),
    ]
LEVEL_CHOICES = [('beg', 'Beginner'), ('adv', 'Advanced')]


class ChooseWordsForm(forms.Form):
    category = forms.CharField(label='Category:', widget=forms.Select(attrs={'class': "custom-drop-list"},
                                                                      choices=CATEGORY_CHOICES))
    level = forms.CharField(label='Level:', widget=forms.RadioSelect(attrs={'class': "custom-radio-list"},
                                                                     choices=LEVEL_CHOICES))


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

