from django import forms
from . import models

class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Book
        fields= ['title','author','body','url_id','thumb']