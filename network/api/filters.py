import django_filters

from network.base.models import Data


class DataViewFilter(django_filters.FilterSet):
    start = django_filters.IsoDateTimeFilter(name='start', lookup_expr='gte')
    end = django_filters.IsoDateTimeFilter(name='end', lookup_expr='lte')
    norad = django_filters.NumberFilter(name='observation__satellite__norad_cat_id',
                                        lookup_expr='iexact')

    class Meta:
        model = Data
        fields = ['ground_station']
