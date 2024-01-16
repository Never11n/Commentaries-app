from django import forms
from captcha.fields import CaptchaField


class UserForm(forms.Form):
    name = forms.CharField(label='Name', max_length=250,)
    email = forms.EmailField(label='Email')
    comment = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 5}))
    captcha = CaptchaField()