from django.conf.urls.defaults import *
from django.contrib import admin
from karpeles.settings import MEDIA_ROOT

admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple',
    (r'^construction/$', 'direct_to_template', {'template':'construction.html'}),
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
)

urlpatterns += patterns('karpeles.content.views',
    (r'^$', 'index'),
    (r'^about/$', 'about'),
    (r'^attorneys/$', 'attorneys'),
    (r'^practice_areas/$', 'practice_areas'),
    (r'^resources/$', 'resources'),
    (r'^contact/$', 'contact'),
)

urlpatterns += patterns('',
    (r'^admin/(.*)$', admin.site.root),
    (r'^site_media/(.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
)

