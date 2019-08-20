from __future__ import absolute_import

import os

from azure.common.credentials import ServicePrincipalCredentials
# for Azure Key Vault
from azure.keyvault import KeyVaultAuthentication, KeyVaultClient
from celery import Celery
from django.conf import settings
from msrestazure.azure_active_directory import MSIAuthentication

credentials = MSIAuthentication(resource='https://vault.azure.net')
client = KeyVaultClient(credentials)

BLOB_STORAGE_CON_STRING = client.get_secret("https://b40.vault.azure.net/",
                        "AZURE-STORAGE-KEY-CON-STRING", "691d5b63e44d41e48dd4a45feb90fc46").value

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'melive.settings')

app = Celery('melive', azureblockblob_container_name = "celery",
        backend=BLOB_STORAGE_CON_STRING, broker='amqp://jm:159753@localhost//')

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
