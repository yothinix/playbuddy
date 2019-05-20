import django_filters

from .models import Program


class ProgramFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='movie__name',
        lookup_expr='icontains'
    )
    channel = django_filters.CharFilter(
        field_name='channel__display_name',
        lookup_expr='icontains'
    )

    class Meta:
        model = Program
        fields = ('name', 'channel')
