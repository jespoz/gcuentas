from django.conf.urls import url, patterns
from .views import *

urlpatterns = patterns('',
    url(r'^$', Lista.as_view(), name='lista_bonos'),
)