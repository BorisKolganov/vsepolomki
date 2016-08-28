from django.conf.urls import url

from cars.views import BreakdownSearch, AjaxCarsModels, AjaxCarsModifications, AjaxBreakdowns, AjaxCarsYears

urlpatterns = [
    url(r'^breakdown_search/$', BreakdownSearch.as_view(), name='breakdown_search'),
    url(r'^get_models/$', AjaxCarsModels.as_view(), name='cars_models'),
    url(r'^get_years/$', AjaxCarsYears.as_view(), name='cars_years'),
    url(r'^get_modifications/$', AjaxCarsModifications.as_view(), name='cars_modifications'),
    url(r'^breakdowns/$', AjaxBreakdowns.as_view(), name='breakdowns'),
]
