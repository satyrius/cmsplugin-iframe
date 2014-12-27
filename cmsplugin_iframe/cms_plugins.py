from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _

from .models import IframePlugin as Plugin
from .forms import IframeForm


class IframePlugin(CMSPluginBase):
    model = Plugin
    form = IframeForm
    name = _('Iframe Video Plugin')
    render_template = 'cms/plugins/iframe.html'

plugin_pool.register_plugin(IframePlugin)
