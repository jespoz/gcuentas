from django.conf.urls import url, patterns
from .views import *

urlpatterns = patterns('',
   url(r'^$', home.as_view(), name='home'),
)
