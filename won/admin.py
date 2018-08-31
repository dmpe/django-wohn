from django.contrib import admin

# Register your models here.
from .models import Users, ApartmentType

admin.site.register(Users)
admin.site.register(ApartmentType)