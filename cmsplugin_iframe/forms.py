from django import forms

from .models import IframePlugin


class IframeForm(forms.ModelForm):
    src = forms.URLField(widget=forms.Textarea)

    class Meta:
        model = IframePlugin
