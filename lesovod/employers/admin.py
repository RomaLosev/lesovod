from django.contrib import admin

from .models import Employers


class EmployersAdmin(admin.ModelAdmin):
    list_display = ('position', 'name')
    search_fields = ('name',)
    list_filter = ('work_since',)


admin.site.register(Employers, EmployersAdmin)
