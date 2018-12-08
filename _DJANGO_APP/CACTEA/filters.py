import django_tables2 as tables
from .models import cactea
import django_filters

class TableFilter(django_filters.FilterSet):
    
    class Meta:
        model = cactea
        fields = [field.name for field in cactea._meta.fields]
