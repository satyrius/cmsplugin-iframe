export PYTHONPATH := $(CURDIR):$(CURDIR)/tests

messages:
	DJANGO_SETTINGS_MODULE=settings_17 \
		source .tox/django-1.7/bin/activate && \
		cd cmsplugin_iframe && \
		django-admin.py makemessages -l en

south_migrations:
	DJANGO_SETTINGS_MODULE=settings_south \
		.tox/django-1.6/bin/django-admin.py \
		schemamigration cmsplugin_iframe --auto || true

migrations:
	DJANGO_SETTINGS_MODULE=settings_17 \
		.tox/django-1.7/bin/django-admin.py \
		makemigrations cmsplugin_iframe
