from django.conf.urls import url

from core.views import Index, About

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^about/$', About.as_view(), name='about')
]
