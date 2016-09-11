from django.conf.urls import url

from breakdown_search.views import BreakdownSearch, TreeSearch, GetPrevNode

urlpatterns = [
    url(r'^breakdown_search/$', BreakdownSearch.as_view(), name='breakdown_search'),
    url(r'^search/$', TreeSearch.as_view(), name='search'),
    url(r'^go_back/$', GetPrevNode.as_view(), name='prev_node')
]
