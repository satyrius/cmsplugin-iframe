export PYTHONPATH := $(CURDIR):$(CURDIR)/tests
export DJANGO_SETTINGS_MODULE := settings

south_migrations:
	DJANGO_SETTINGS_MODULE=settings_south \
		.tox/django-1.6/bin/django-admin.py \
		schemamigration cmsplugin_iframe --auto || true

migrations:
	DJANGO_SETTINGS_MODULE=settings_17 \
		.tox/django-1.7/bin/django-admin.py \
		makemigrations cmsplugin_iframe
