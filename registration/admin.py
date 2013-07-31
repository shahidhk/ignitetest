# Register the data to be shown in admin page
from django.contrib import admin
from registration.models import *
from ignitetest.actions import export_as_xls


admin.site.register(School)


class StudentAdmin(admin.ModelAdmin):
    actions = [export_as_xls]

admin.site.register(Student, StudentAdmin)