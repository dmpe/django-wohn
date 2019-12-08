"""
    Used for local development
"""

import os

SECRET_KEY = "1h1pi2se&=1!5sd6zdm%x-vm*4=mj+)900i%w*s=rya5c^9tot"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "loggers": {"django": {"handlers": ["console"], "level": os.getenv("DJANGO_LOG_LEVEL", "INFO")}},
}

# the curpit: on local pc must be local database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "mydb",
        "USER": "jm",
        "PASSWORD": "123",
        "HOST": "localhost",
        "PORT": "",
    }
}
