from django.contrib.gis import admin

from .models import School

admin.site.register(School, admin.GISModelAdmin)
