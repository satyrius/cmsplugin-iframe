================
cmsplugin-iframe
================

|ci|

.. |ci| image:: https://travis-ci.org/satyrius/cmsplugin-iframe.png?branch=master
    :target: https://travis-ci.org/satyrius/cmsplugin-iframe

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
