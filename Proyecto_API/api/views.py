from typing import Any
from django import http
from django.http import JsonResponse
from django.views import View
from .models import Company
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


class CompanyView(View):
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
        return JsonResponse(datos)
