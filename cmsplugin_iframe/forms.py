import re

from bs4 import BeautifulSoup
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import IframePlugin


class EmbedURLField(forms.URLField):
    widget = forms.Textarea

    def clean(self, value):
        if re.search(r'<iframe', value, re.IGNORECASE):
            soup = BeautifulSoup(value)
            src = soup.iframe.get('src')
            if not src:
                raise forms.ValidationError(
                    _('The `iframe` HTML snippet was passed, but there is no '
                      '`src` arrtibute was found'),
                    code='invalid')
            value = src
        return super(EmbedURLField, self).clean(value)


class IframeForm(forms.ModelForm):
    src = EmbedURLField(
        label=_('Embed'),
        help_text=_('Embed url or whole html embed code'))

    class Meta:
        model = IframePlugin
