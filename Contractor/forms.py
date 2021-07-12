from django.core import validators
from django import forms
from .models import Contractor


class ContractorRegister(forms.ModelForm):
    class Meta:
        model = Contractor
        fields = ["cid","name", "city","zipcode"]
        widgets = {
            "cid": forms.TextInput(attrs={"class": "form-control form-control-sm"}),
            "name": forms.TextInput(attrs={"class": "form-control form-control-sm"}),
            "city": forms.TextInput(attrs={"class": "form-control form-control-sm"}),
            "zipcode": forms.TextInput(attrs={"class": "form-control form-control-sm"}),
        }