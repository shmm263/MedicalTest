import django_filters
from .models import Patient

class PosteFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    addr_city = django_filters.CharFilter(lookup_expr='icontains')
    phone_mobile = django_filters.CharFilter(name='phone_mobile', lookup_expr='icontains')
    class Meta:
       model = Patient
       fields = {'first_name', 'addr_city', 'phone_mobile',}