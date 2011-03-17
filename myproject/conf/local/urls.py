from django.conf import settings
from django.conf.urls.defaults import include, patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
    url(r'', include('myproject.urls')),
    url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True
        }),
)

urlpatterns += staticfiles_urlpatterns()
