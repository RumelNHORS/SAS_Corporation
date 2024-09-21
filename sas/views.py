from django.shortcuts import render
from rest_framework import generics
from sas import serializers as sas_serializers
from sas import models as sas_models



# List all services and create a new service
class ServiceListCreateView(generics.ListCreateAPIView):
    queryset = sas_models.Service.objects.all()
    serializer_class = sas_serializers.ServiceSerializer


# Retrieve, update, or delete a specific service by ID
class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = sas_models.Service.objects.all()
    serializer_class = sas_serializers.ServiceSerializer
