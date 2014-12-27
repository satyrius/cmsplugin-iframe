export PYTHONPATH := $(CURDIR):$(CURDIR)/tests
export DJANGO_SETTINGS_MODULE := settings_17

messages:
	source .tox/django-1.7/bin/activate && \
	cd cmsplugin_iframe && \
	django-admin.py makemessages -l en

south_migrations:
	DJANGO_SETTINGS_MODULE=settings_south \
	source .tox/django-1.6/bin/activate && \
	django-admin.py schemamigration cmsplugin_iframe --auto || true

migrations:
	source .tox/django-1.7/bin/activate && \
	django-admin.py makemigrations cmsplugin_iframe
