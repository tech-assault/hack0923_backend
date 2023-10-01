import os
import sys

from celery import Celery

sys.path.append("../")


# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "forecast.settings")

from django.conf import settings  # noqa

app = Celery("forecast")

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
