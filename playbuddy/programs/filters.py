import django_filters
import pendulum

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
    now_showing = django_filters.BooleanFilter(
        method='now_showing_filter'
    )

    def now_showing_filter(self, queryset, name, value):
        if name == 'now_showing' and value is True:
            now = pendulum.now()
            return queryset.filter(
                date=now.date(),
                start_time__lt=now.time(),
                end_time__gt=now.time()
            )
        else:
            return queryset

    class Meta:
        model = Program
        fields = ('name', 'channel', 'date')
