"""
This is a django-split-settings main file.

For more information read this:
https://github.com/sobolevn/django-split-settings

Close copy of https://medium.com/wemake-services/managing-djangos-settings-e2b7f496120d

Default environment is `developement`.

To change settings file:
`DJANGO_ENV=production python manage.py runserver`
"""
from split_settings.tools import optional, include
from os import environ

ENV = environ.get('DJANGO_ENV') or 'development'

base_settings = [
    'components/common.py',  # standard django settings

    # Select the right env:
    'environments/%s.py' % ENV,

    # Optionally override some settings:
    # optional('environments/local.py'),
]

# Include settings:
include(*base_settings)