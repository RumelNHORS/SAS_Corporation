from django.urls import path
from sas import views as sas_views


urlpatterns = [
    path('services/', sas_views.ServiceListCreateView.as_view(), name='service_list_create'),
    path('services/<int:pk>/', sas_views.ServiceDetailView.as_view(), name='service_detail'),

    path('business_partners/', sas_views.BusinessPartnerListCreateAPIView.as_view(), name='business_partner_list_create'),
    path('business_partners/<int:pk>/', sas_views.BusinessPartnerRetrieveUpdateDestroyAPIView.as_view(), name='business_partner_detail'),

    path('projects/', sas_views.ProjectListCreateAPIView.as_view(), name='project_list_create'),
    path('projects/<int:pk>/', sas_views.ProjectRetrieveUpdateDestroyAPIView.as_view(), name='project_detail'),

    path('sas_gallery/', sas_views.SasGalleryListCreateAPIView.as_view(), name='sas_gallery_list_create'),
    path('sas_gallery/<int:pk>/', sas_views.SasGalleryRetrieveUpdateDestroyAPIView.as_view(), name='sas_gallery_detail'),

    path('about_sas/', sas_views.AboutUsListCreateAPIView.as_view(), name='about_sas'),
    path('about_sas/<int:pk>/', sas_views.AboutUsRetriveUpdateDestroyAPIView.as_view(), name='about_detail'),

    path('sas_info/', sas_views.SasInfoListCreateListAPIView.as_view(), name='sas_info'),
    path('sas_info/<int:pk>/', sas_views.SasInfoRetriveUpdateDestroyAPIIView.as_view(), name='sas_info_detail'),

    path('testimonials/', sas_views.TestimonialListCreateView.as_view(), name='testimonial_list_create'),
    path('testimonials/<int:pk>/', sas_views.TestimonialRetrieveUpdateDestroyView.as_view(), name='testimonial_detail'),

    path('our_clients/', sas_views.OurClientListCreateView.as_view(), name='our_client_list_create'),
    path('our_clients/<int:pk>/', sas_views.OurClientRetrieveUpdateDestroyView.as_view(), name='our_client_detail'),

    path('our_team/', sas_views.OurTeamListCreateView.as_view(), name='our_team'),
    path('our_team/<int:pk>/', sas_views.OurTeamRetrieveUpdateDestroyView.as_view(), name='our_team_details'),

    path('it_criticism/', sas_views.OurITSectionListCreateView.as_view(), name='it_criticism'),
    path('it_criticism/<int:pk>/', sas_views.OurITSectionRetrieveUpdateDestroyView.as_view(), name='it_criticism_details'),
    
]