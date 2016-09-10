from itertools import groupby

from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from itertools import chain
# Create your views here.
from django.views.generic import TemplateView, View
from cars.models import CarBrand, CarModel, CarModification, BreakdownType, Breakdown
from services.models import Service, Work

class BreakdownSearch(TemplateView):
    template_name = 'breakdown_search.html'

    def get_context_data(self, **kwargs):
        context = super(BreakdownSearch, self).get_context_data(**kwargs)
        context['cars_brands'] = CarBrand.objects.all()
        return context


class AjaxCarsModels(View):
    def get(self, request):
        try:
            brand_id = int(request.GET.get('brand_id'))
        except (ValueError, TypeError):
            return HttpResponseBadRequest()
        models = CarModel.objects.filter(brand_id=brand_id)
        return JsonResponse({"models": [{"id": model.id, "name": model.name} for model in models]})


class AjaxCarsYears(View):
    def get(self,  request):
        try:
            model_id = int(request.GET.get('model_id'))
        except (ValueError, TypeError):
            return HttpResponseBadRequest()
        cms = CarModification.objects.filter(car_model_id=model_id)
        intervals = [(cm.year_from, cm.year_to + 1) for cm in cms]
        years_list = chain.from_iterable([[i for i in range(*interval)] for interval in intervals])
        return JsonResponse({
            "years": sorted(set(years_list))
        })


class AjaxCarsModifications(View):
    def get(self, request):
        try:
            model_id = int(request.GET.get('model_id'))
            year = int(request.GET.get('year'))
        except (ValueError, TypeError):
            return HttpResponseBadRequest()
        modifications = CarModification.objects.filter(car_model_id=model_id, year_from__lte=year, year_to__gte=year)
        return JsonResponse({"modifications": [{"id": modification.id, "name": modification.__unicode__()} for modification in modifications]})


class AjaxBreakdowns(View):
    def get(self, request):
        context = {'breakdowns': []}
        breakdowns = Breakdown.objects.all().select_related('breakdown_type')
        for k, group in groupby(breakdowns, lambda x: x.breakdown_type):
            breakdown = {
                'text': k.name,
                'nodes': []
            }
            for g in group:
                breakdown['nodes'].append({
                    'text': g.name,
                    'href': '#' + str(g.id)
                })
            context['breakdowns'].append(breakdown)
        return JsonResponse(context)


class AjaxBreakdown(View):
    def get(self, request):
        try:
            breakdown_id = int(request.GET.get('breakdown_id'))
        except (ValueError, TypeError):
            return HttpResponseBadRequest()
        breakdown = get_object_or_404(Breakdown, id=breakdown_id)
        services_list = Work.objects.filter(breakdown_id=breakdown_id).values_list('service', flat=True)
        services = Service.objects.filter(id__in=services_list)
        services = [service.as_dict(breakdown.id) for service in services]
        context = {'breakdown': breakdown.as_dict(price=True), 'services': services}
        return JsonResponse(context)
