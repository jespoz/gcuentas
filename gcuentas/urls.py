from django.conf.urls import include, url, patterns
from django.conf import settings
from django.contrib import admin

urlpatterns = patterns('',
                       (r'static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
                       (r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
                       url(r'^admin/', include(admin.site.urls)),
)
