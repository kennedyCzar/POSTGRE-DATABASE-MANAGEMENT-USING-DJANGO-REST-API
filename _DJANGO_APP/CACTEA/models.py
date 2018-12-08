from django.db import models

# Create your models here.

class cactea(models.Model):
    id_IT = models.CharField(max_length = 100, primary_key=True)
    SERIAL_NUMBER = models.CharField(max_length = 100)
    MANUFACTURER = models.CharField(max_length = 100)
    NAME = models.CharField(max_length = 100)
    MODEL = models.CharField(max_length = 100)
    LOCATION = models.CharField(max_length = 100)
    ROOM = models.CharField(max_length = 100)
    ENERGY_CONSUMPTION = models.CharField(max_length = 100)
    BTU = models.CharField(max_length = 100)
    MICROCODE = models.CharField(max_length = 100)
    PATCH_LEVEL = models.CharField(max_length = 100)
    CUSTOMER_ID = models.CharField(max_length = 100)
    HOSTS_APPLICATION = models.CharField(max_length = 100)
    TCPADDR1 = models.CharField(max_length = 100)
    TCPADDR2 = models.CharField(max_length = 100)
    TCPADDR3 = models.CharField(max_length = 100)
    SW_GUI = models.CharField(max_length = 100)
    INVESTMENT_DATE = models.CharField(max_length = 100)
    MAINTENANCE_EXPIRATION_DATE = models.CharField(max_length = 100)
    MAINTENANCE_PROVIDER = models.CharField(max_length = 100)
    MAINTENANCE_CONTRACT = models.CharField(max_length = 100)
    IS_EXTENSION_REQUIRED = models.CharField(max_length = 100)
    IS_MIGRATION_REQUIRED = models.CharField(max_length = 100)
    RAID_CONFIG = models.CharField(max_length = 100)
    USABLE_CAPACITY_GB = models.CharField(max_length = 100)
    CAPACITY_IN_USE_GB = models.CharField(max_length = 100)
    FREE_CAPACITY_GB = models.CharField(max_length = 100)
    EXTENSION = models.CharField(max_length = 100)
    COMMENT_1 = models.CharField(max_length = 100)
    STORAGE_TYPE = models.CharField(max_length = 100)
    READADMIN = models.CharField(max_length = 100)
    RACK = models.CharField(max_length = 100)
    COST_CENTER = models.CharField(max_length = 100)
    CO2_KG = models.CharField(max_length = 100)
    SECOND_INVESTMENT_DATE = models.CharField(max_length = 99)

    class Meta:
        verbose_name = 'cactea'
        verbose_name_plural = 'cacteas'
        ordering = ['id_IT']
        
    def __str__(self):
        return self.NAME