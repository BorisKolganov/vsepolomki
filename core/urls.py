from django.conf.urls import url

from core.views import Index

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
]
