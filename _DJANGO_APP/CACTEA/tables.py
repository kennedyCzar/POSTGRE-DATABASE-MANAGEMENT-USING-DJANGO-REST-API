import django_tables2 as tables
from .models import cactea
from import_export import resources

class CacteaTable(tables.Table):
    
    class Meta:
        model = cactea
        

class CacResource(resources.ModelResource):
    
    class Meta:
        model = cactea