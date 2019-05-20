from django.contrib import admin

from .models import Program


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('movie_name', 'channel_name', 'date', 'start_time', 'end_time',)
    list_filter = ('channel__display_name', 'date',)
    search_fields = ('movie__name',)
