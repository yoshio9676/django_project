from django import forms
from .models import SnsModel

class SnsForm(forms.ModelForm):
    class Meta:
        model = SnsModel
        fields = ('title', 'content', 'author', 'snsimage')