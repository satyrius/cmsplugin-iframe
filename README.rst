================
cmsplugin-iframe
================

|ci| |pypi| |status|

.. |ci| image:: https://travis-ci.org/satyrius/cmsplugin-iframe.png?branch=master
    :target: https://travis-ci.org/satyrius/cmsplugin-iframe

.. |pypi| image:: https://pypip.in/version/cmsplugin-iframe/badge.png?text=pypi
    :target: https://pypi.python.org/pypi/cmsplugin-iframe/
    :alt: Latest Version

.. |status| image:: https://pypip.in/status/cmsplugin-iframe/badge.png
    :target: https://pypi.python.org/pypi/cmsplugin-iframe/
    :alt: Development Status


All major video hosters like *YouTube* and *Vemeo* has embed codes as *html iframe* snippets.
This Django CMS plugin allows you to add video iframe to the page (actually you can add any page as iframe, not only video).

Requirements
============

It works fine and tested under ``Python 2.7``. The following libraries are required

- ``Django`` >= 1.5
- ``django-cms`` >= 3.0 (we recommend to use Django CMS 3.0 and higher, contact us if you need prior CMS versions supports and have some issues)
- ``beautifulsoup4`` for iframe embed snippets parsing

Installation
============

::

$ pip install cmsplugin-iframe

Configure installed apps in your ``settings.py`` ::

  INSTALLED_APPS = [
      # django contrib and django cms apps
      'cmsplugin_iframe',
  ]

Migrate your database ::

  django-admin.py migrate cmsplugin_iframe

Usage
=====

Add plugin to the page with common way. You can specify video by URL or give plugin an iframe html snippet to parse. 
To customize how it looks you can override `cms/plugins/iframe.html`.

Roadmap
=======
- Python 3 support

Changelog
=========
The changelog can be found at `repo's release notes <https://github.com/satyrius/cmsplugin-iframe/releases>`_

Contributing
============
Fork the repo, create a feature branch then send me pull request. Feel free to create new issues or contact me via email.

Translation
-----------
You could also help me to translate `cmsplugin-iframe` to your native language `with Transifex <https://www.transifex.com/projects/p/cmsplugin-iframe/resource/main/>`_
