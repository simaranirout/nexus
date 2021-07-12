from django.core import validators
from django import forms
from .models import Job


class IjRegister(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["jid","jobTitle", "jobPrice","company","contractor","jobtime"]
        widgets = {
            "jid": forms.TextInput(attrs={"class": "form-control form-control-sm"}),
            "jobTitle": forms.TextInput(attrs={"class": "form-control form-control-sm"}),
            "jobPrice": forms.TextInput(attrs={"class": "form-control form-control-sm"}),
            "jobtime":forms.DateInput(attrs={'class': 'form-control', 
                       'placeholder': 'Enter time In 24 format',
                       'type': 'text' 
                      }),
        }
    