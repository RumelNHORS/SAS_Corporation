from rest_framework import serializers
from sas import models as sas_models
from django.utils.html import strip_tags
import html



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
    clean_message = serializers.SerializerMethodField()
    class Meta:
        model = sas_models.SasInfo
        fields = ['id', 'address', 'facebook', 'instagram', 'linkedin', 'twitter', 'tiktok', 'pinterest']

    def get_clean_message(self, obj):
        # Strip any HTML tags from the message
        clean_message = strip_tags(obj.message)
        return html.unescape(clean_message)


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = sas_models.Testimonial
        fields = ['id', 'name', 'designation', 'message', 'image', 'created_at']


class OurClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = sas_models.OurClient
        fields = ['id', 'image']

# Our Team Serializer
class OurTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = sas_models.OurTeam
        fields = '__all__'


# Our IT/Criticism
class OurITSectionSerializer(serializers.ModelSerializer):
    class Meta:
        Model = sas_models.OurITSection
        fields = '__all__'
