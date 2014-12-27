import unittest
from cmsplugin_iframe.forms import IframeForm


class IframeFormTest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://www.youtube.com/embed/RRpDn5qPp3s'

    def test_url_as_is(self):
        form = IframeForm(data={'src': self.url})
        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(form.cleaned_data['src'], self.url)

    def test_extract_from_embed_code(self):
        emded_code = '''
            <iframe width="560" height="315" src="{url}"
                frameborder="0" allowfullscreen></iframe>
        '''.format(url=self.url).strip()
        form = IframeForm(data={'src': emded_code})
        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(form.cleaned_data['src'], self.url)

    def test_extract_from_embed_code_single_quote(self):
        emded_code = '''
            <iframe width='560' height='315' src='{url}'
                frameborder='0' allowfullscreen></iframe>
        '''.format(url=self.url).strip()
        form = IframeForm(data={'src': emded_code})
        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(form.cleaned_data['src'], self.url)

    def test_iframe_without_src(self):
        emded_code = '''
            <iframe frameborder="0" allowfullscreen></iframe>
        '''.format(url=self.url).strip()
        form = IframeForm(data={'src': emded_code})
        self.assertFalse(form.is_valid())
        self.assertIn('src', form.errors)
