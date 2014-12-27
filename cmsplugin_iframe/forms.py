import re

from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import IframePlugin


class EmbedURLField(forms.URLField):
    widget = forms.Textarea

    def clean(self, value):
        if re.search(r'<iframe', value, re.IGNORECASE):
            m = re.search(r'src="([^"]+)"', value)
            if not m:
                raise forms.ValidationError(
                    _('The `iframe` HTML snippet was passed, but there is no '
                      '`src` arrtibute was found'),
                    code='invalid')
            value = m.group(1)
        return super(EmbedURLField, self).clean(value)


class IframeForm(forms.ModelForm):
    src = EmbedURLField()

    class Meta:
        model = IframePlugin
