from django.urls import path
#from .views import CompanyView
from .views import LicenciamientoView

urlpatterns = [
    #path('companies/', CompanyView.as_view(), name='companies_list'),
    #path('companies/<int:id>', CompanyView.as_view(), name='companies_process'),

    path('licenciameinto/', LicenciamientoView.as_view(), name='licenciamiento_list'),
    path('licenciameinto/<int:id_licencia>', LicenciamientoView.as_view(), name='licenciamiento_process'),
]