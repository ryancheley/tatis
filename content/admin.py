from django.contrib import admin

from .models import InjuredList, SuspendedList

admin.site.register(InjuredList)
admin.site.register(SuspendedList)
