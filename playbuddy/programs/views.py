from datetime import date

from django.shortcuts import render
from django.views.generic import ListView

from .filters import ProgramFilter
from .models import Program


class ProgramView(ListView):
    model = Program
    paginate_by = 30
    context_object_name = 'programs'

    def get_queryset(self):
        qs = Program.objects.all()
        program_filter_list = ProgramFilter(self.request.GET, queryset=qs)
        return program_filter_list.qs
