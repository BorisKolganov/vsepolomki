from itertools import groupby

from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, View
from cars.models import CarBrand, CarModel, CarModification, BreakdownType, Breakdown


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


class AjaxCarsModifications(View):
    def get(self, request):
        try:
            model_id = int(request.GET.get('model_id'))
        except (ValueError, TypeError):
            return HttpResponseBadRequest()
        modifications = CarModification.objects.filter(car_model_id=model_id)
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
                    'text': g.name
                })
            context['breakdowns'].append(breakdown)
        return JsonResponse(context)