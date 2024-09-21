from rest_framework import serializers
from sas import models as sas_models



class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = sas_models.Service
        fields = ['id', 'icon', 'title', 'description']