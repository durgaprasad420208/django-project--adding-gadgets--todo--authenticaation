from django import forms
from . import models


class ComputerForm(forms.ModelForm):
    class Meta:
        model = models.Computer
        fields = "__all__"


class BrandForm(forms.ModelForm):
    class Meta:
        model = models.Brand
        fields = ['name']
