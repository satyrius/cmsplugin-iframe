import unittest
from cmsplugin_iframe.forms import IframeForm


class IframeFormTest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://www.youtube.com/embed/RRpDn5qPp3s'

    def test_url_as_is(self):
        form = IframeForm(data={'src': self.url})
        self.assertTrue(form.is_valid(), form.errors)
