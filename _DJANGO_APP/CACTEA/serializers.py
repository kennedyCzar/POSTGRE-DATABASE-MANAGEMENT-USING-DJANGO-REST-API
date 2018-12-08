from rest_framework import serializers
from .models import cactea


class CacteaSerializer(serializers.ModelSerializer):
    class Meta:
        model  = cactea
        fields = ("id_IT",
                "SERIAL_NUMBER",
                "MANUFACTURER",
                "NAME",
                "MODEL",
                "LOCATION",
                "ROOM",
                "ENERGY_CONSUMPTION",
                "BTU",
                "MICROCODE",
                "PATCH_LEVEL",
                "CUSTOMER_ID",
                "HOSTS_APPLICATION",
                "TCPADDR1",
                "TCPADDR2",
                "TCPADDR3",
                "SW_GUI",
                "INVESTMENT_DATE",
                "MAINTENANCE_EXPIRATION_DATE",
                "MAINTENANCE_PROVIDER",
                "MAINTENANCE_CONTRACT",
                "IS_EXTENSION_REQUIRED",
                "IS_MIGRATION_REQUIRED",
                "RAID_CONFIG",
                "USABLE_CAPACITY_GB",
                "CAPACITY_IN_USE_GB",
                "FREE_CAPACITY_GB",
                "EXTENSION",
                "COMMENT_1",
                "STORAGE_TYPE",
                "READADMIN",
                "RACK",
                "COST_CENTER",
                "CO2_KG",
                "SECOND_INVESTMENT_DATE",)


class ToUpperCaseCharField(serializers.CharField):
    def to_representation(self, value):
        return value.upper()