from django import forms
from .models import Word

class AnswerWord(forms.Form):
    translation = forms.CharField(label='translation', max_length=100)

