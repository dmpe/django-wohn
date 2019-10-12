"""
    An empty shell
"""
import os, sys
import dj_database_url

SECRET_KEY = "1h1pi2se&=1!5sd6zdm%x-vm*4=mj+)900i%w*s=rya5c^9tot"

DATABASES = None
DATABASES = { 'default': dj_database_url.condig(default="postgres://postgres:django@postgres:5432/b40re", conn_max_age=600)}


# DATABASES["default"] = dj_database_url.parse(
#     "postgres://postgres:django@postgres:5432/b40re", conn_max_age=600
# )
