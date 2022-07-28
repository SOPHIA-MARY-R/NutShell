from django.contrib import admin
from .models import URL
# Register your models here.
'''
The Django admin is an automatically-generated user interface for Django models.
The register function is used to add models to the Django admin so that data for
those models can be created, deleted, updated and queried through the user interface.
'''
admin.site.register(URL)