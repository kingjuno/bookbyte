from django import forms
from . import models

class CreateReq(forms.ModelForm):
    class Meta:
        model = models.Req
        fields= ['title','author','url_id']