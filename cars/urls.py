from django.conf.urls import url

from cars.views import BreakdownSearch

urlpatterns = [
    url(r'^breakdown_search/$', BreakdownSearch.as_view(), name='breakdown_search'),
]
