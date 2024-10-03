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


# List all SasGallery items or create a new one
class SasGalleryListCreateAPIView(generics.ListCreateAPIView):
    queryset = sas_models.SasGallery.objects.all()
    serializer_class = sas_serializers.SasGallerySerializer


# Retrieve, update, or delete a specific SasGallery item by ID
class SasGalleryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = sas_models.SasGallery.objects.all()
    serializer_class = sas_serializers.SasGallerySerializer


# About us View
class AboutUsListCreateAPIView(generics.ListCreateAPIView):
    queryset = sas_models.AboutUs.objects.all()
    serializer_class = sas_serializers.AboutUsSerializer


class AboutUsRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = sas_models.AboutUs.objects.all()
    serializer_class = sas_serializers.AboutUsSerializer


class SasInfoListCreateListAPIView(generics.ListCreateAPIView):
    queryset = sas_models.SasInfo.objects.all()
    serializer_class = sas_serializers.SasInfoSerializer


class SasInfoRetriveUpdateDestroyAPIIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = sas_models.SasInfo.objects.all()
    serializer_class = sas_serializers.SasInfoSerializer


# List all testimonials and create a new one
class TestimonialListCreateView(generics.ListCreateAPIView):
    queryset = sas_models.Testimonial.objects.all()
    serializer_class = sas_serializers.TestimonialSerializer


# Retrieve, update, or delete a specific testimonial
class TestimonialRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = sas_models.Testimonial.objects.all()
    serializer_class = sas_serializers.TestimonialSerializer


# List all clients and create a new one
class OurClientListCreateView(generics.ListCreateAPIView):
    queryset = sas_models.OurClient.objects.all()
    # serializer_class = sas_serializers.TestimonialSerializer
    serializer_class = sas_serializers.OurClientSerializer

# Retrieve, update, or delete a specific client
class OurClientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = sas_models.OurClient.objects.all()
    serializer_class = sas_serializers.OurClientSerializer


# View for OurTeam
class OurTeamListCreateView(generics.ListCreateAPIView):
    queryset = sas_models.OurTeam.objects.all()
    serializer_class = sas_serializers.OurTeamSerializer


class OurTeamRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = sas_models.OurTeam.objects.all()
    serializer_class = sas_serializers.OurTeamSerializer


# Our IT/Criticism View
class OurITSectionListCreateView(generics.ListCreateAPIView):
    queryset = sas_models.OurITSection.objects.all()
    serializer_class = sas_serializers.OurITSectionSerializer
