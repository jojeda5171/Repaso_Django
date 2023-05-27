from typing import Any
from django import http
from django.http import JsonResponse
from django.views import View
#from .models import Company
from .models import licenciameinto
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
class LicenciamientoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id_licencia=0):
        if id_licencia > 0:
            licencias = list(licenciameinto.objects.filter(id_licencia=id_licencia).values())
            if len(licencias) > 0:
                licencia = licencias[0]
                datos = {'mesaje': 'Success', 'licencia': licencia}
            else:
                datos = {'mesaje': 'No hay datos'}
            return JsonResponse(datos)
        else:
            licencias = list(licenciameinto.objects.values())
            if len(licencias) > 0:
                datos = {'mesaje': 'Success', 'licencias': licencias}
            else:
                datos = {'mesaje': 'No hay datos'}
            return JsonResponse(datos)

    def post(self, request):
        # print (request.body)
        jd = json.loads(request.body)
        #print (jd)
        licenciameinto.objects.create(
            licencia=jd['licencia'], estado=jd['estado'], fecha_emision=jd['fecha_emision'], fecha_vencimiento=jd['fecha_vencimiento'])
        datos = {'mensaje': 'Success'}
        return JsonResponse(datos)

    def put(self, request, id_licencia):
        jd = json.loads(request.body)
        licencias = list(licenciameinto.objects.filter(id_licencia=id_licencia).values())
        if len(licencias) > 0:
            licencia=licenciameinto.objects.get(id_licencia=id_licencia)
            licencia.licencia=jd['licencia']
            licencia.estado=jd['estado']
            licencia.fecha_emision=jd['fecha_emision']
            licencia.fecha_vencimiento=jd['fecha_vencimiento']
            licencia.save()
            datos = {'mensaje': 'Success'}
        else:
            datos = {'mensaje': 'No hay datos'}
        return JsonResponse(datos)
    def delete(self, request, id_licencia):
        licencias=list(licenciameinto.objects.filter(id_licencia=id_licencia).values())
        if len(licencias)>0:
            licencia=licenciameinto.objects.get(id_licencia=id_licencia)
            licencia.delete()
            datos={'mensaje':'Success'}
        else:
            datos={'mensaje':'No hay datos'}
        return JsonResponse(datos)

""" class CompanyView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            companies = list(Company.objects.filter(id=id).values())
            if len(companies) > 0:
                company = companies[0]
                datos = {'mesaje': 'Success', 'company': company}
            else:
                datos = {'mesaje': 'No hay datos'}
            return JsonResponse(datos)
        else:
            companies = list(Company.objects.values())
            if len(companies) > 0:
                datos = {'mesaje': 'Success', 'companies': companies}
            else:
                datos = {'mesaje': 'No hay datos'}
            return JsonResponse(datos)

    def post(self, request):
        # print (request.body)
        jd = json.loads(request.body)
        # print (jd)
        Company.objects.create(
            name=jd['name'], website=jd['website'], fundation=jd['fundation'])
        datos = {'mensaje': 'Success'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        companies = list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            company=Company.objects.get(id=id)
            company.name=jd['name']
            company.website=jd['website']
            company.fundation=jd['fundation']
            company.save()
            datos = {'mensaje': 'Success'}
        else:
            datos = {'mensaje': 'No hay datos'}
        return JsonResponse(datos)
    def delete(self, request, id):
        companies=list(Company.objects.filter(id=id).values())
        if len(companies)>0:
            company=Company.objects.get(id=id)
            company.delete()
            datos={'mensaje':'Success'}
        else:
            datos={'mensaje':'No hay datos'}
        return JsonResponse(datos) """

