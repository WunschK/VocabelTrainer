from django import forms
from .models import Word, CustomUser


class AnswerWord(forms.Form):
    translation = forms.CharField(label='translation', max_length=100)


class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()

class SignUpForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']  # You can add more fields as needed
        widgets = {'password': forms.PasswordInput(), }