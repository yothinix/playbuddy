from datetime import date

from django.shortcuts import render
from django.views.generic import ListView

from .models import Program


class ProgramView(ListView):
    model = Program
    queryset = Program.objects \
        .filter(channel__display_name='HBO HD', date=date.today()) \
        .order_by('-start_time')

    paginate_by = 10
    context_object_name = 'programs'
