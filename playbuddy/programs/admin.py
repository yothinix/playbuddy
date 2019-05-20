from django.contrib import admin

from .models import Program


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'start_time', 'end_time',)
    list_filter = ('start_time', 'end_time', 'date')
    search_fields = ('movie__name',)
