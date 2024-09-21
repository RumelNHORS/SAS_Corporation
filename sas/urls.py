from django.urls import path
from sas import views as sas_views


urlpatterns = [
    path('services/', sas_views.ServiceListCreateView.as_view(), name='service_list_create'),
    path('services/<int:pk>/', sas_views.ServiceDetailView.as_view(), name='service_detail'),
]