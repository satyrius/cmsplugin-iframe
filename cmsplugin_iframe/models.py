from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class IframePlugin(CMSPlugin):
    src = models.URLField(_('iframe src attribute, video player url'))
