from django.contrib import admin
from .models import cactea
# Register your models here.


class cactea_display(admin.ModelAdmin):
    list_display =  [field.name for field in cactea._meta.fields]
    
admin.site.register(cactea, cactea_display)
