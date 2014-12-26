from django.conf.urls import *  # NOQA

urlpatterns = patterns('',  # NOQA
    url(r'^', include('cms.urls')),
)
