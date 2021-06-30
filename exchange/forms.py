from django import forms
from . import models

class CreateLoc(forms.ModelForm):
    class Meta:
        model = models.Location
        fields= ['message','location','bk']