"""
This is a django-split-settings main file.

For more information read this:
https://github.com/sobolevn/django-split-settings

Close copy of https://medium.com/wemake-services/managing-djangos-settings-e2b7f496120d

Default environment is `development`.

To change settings file: `DJANGO_ENV=production python manage.py runserver`

"""
from os import environ
from split_settings.tools import include, optional
from backend.az_connect import AzureConnection

azCon = AzureConnection()
azCon.main()

base_settings = [
    # Select the right env:
    "environments/%s.py" % azCon.env,
    # standard django settings
    "components/common.py",

    # Optionally override some settings:
    # optional('environments/local.py'),
]
print(azCon.env)
include(*base_settings)
