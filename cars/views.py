from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class BreakdownSearch(TemplateView):
    template_name = 'breakdown_search.html'
