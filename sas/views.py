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


# List all BusinessPartners or create a new one
class BusinessPartnerListCreateAPIView(generics.ListCreateAPIView):
    queryset = sas_models.BusinessPartner.objects.all()
    serializer_class = sas_serializers.BusinessPartnerSerializer
    

# Retrieve, update, or delete a specific BusinessPartner by ID
class BusinessPartnerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = sas_models.BusinessPartner.objects.all()
    serializer_class = sas_serializers.BusinessPartnerSerializer


# List all project or create new project
class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = sas_models.Projects.objects.all()
    serializer_class = sas_serializers.ProjectSerializer


# Retrive, update or Delete Specific Project ny ID
class ProjectRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = sas_models.Projects.objects.all()
    serializer_class = sas_serializers.ProjectSerializer


