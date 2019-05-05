from __future__ import absolute_import
import os
from django.conf import settings
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vanoce.settings')

app = Celery('vanoce', backend='amqp', broker='amqp://jm@localhost//')

# This reads, e.g., CELERY_ACCEPT_CONTENT = ['json'] from settings.py:
app.config_from_object('django.conf:settings')

# For autodiscover_tasks to work, you must define your tasks in a file called 'tasks.py'.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
	print("Request: {0!r}".format(self.request))

app.conf.update(
	result_expires=3600,
	timezone = 'Europe/Prague'
)

if __name__ == '__main__':
	app.start()