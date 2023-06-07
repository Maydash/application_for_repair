from django import forms
from .models import ApplicationForPrinter
from captcha.fields import CaptchaField


class ApplicationForPrinterModelForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = ApplicationForPrinter
        fields = ['name', 'cabinet', 'phone_number', 'problem', 'note']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'cabinet': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'problem': forms.Select(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),

        }