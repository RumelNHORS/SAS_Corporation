from rest_framework import serializers
from sas import models as sas_models



class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = sas_models.Service
        fields = ['id', 'icon', 'title', 'description']



class BusinessPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = sas_models.BusinessPartner
        fields = ['id', 'name', 'image', 'description', 'website_link']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = sas_models.Projects
        fields = ['id', 'project_name', 'project_link', 'description', 'project_image']

class SasGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = sas_models.SasGallery
        fields = ['id', 'title', 'picture']


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = sas_models.AboutUs
        fields = ['id', 'title', 'description', 'image']


class SasInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = sas_models.SasInfo
        fields = ['id', 'address', 'facebook', 'instagram', 'linkedin', 'twitter', 'tiktok', 'pinterest']