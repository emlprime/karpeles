from django.conf.urls.defaults import *
from django.contrib import admin
from karpeles.settings import MEDIA_ROOT
from karpeles.content.models import PracticeArea

admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple',
    (r'^construction/$', 'direct_to_template', {'template':'construction.html'}),
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
)

practice_areas = PracticeArea.objects.all()

urlpatterns += patterns('karpeles.content.views',
    (r'^$', 'index'),
    (r'^about/$', 'about'),
    (r'^attorneys/$', 'attorneys'),
    (r'^practice_areas/$', 'practice_areas'),
    (r'^resources/$', 'resources'),
    (r'^contact/$', 'contact'),
    (r'^disclaimer/$', 'disclaimer'),
)

urlpatterns += patterns('',
    (r'^admin/(.*)$', admin.site.root),
    (r'^site_media/(.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
)

urlpatterns += patterns ('django.views.generic.list_detail',
    (r'^practice_areas/(?P<slug>[a-z_]+)/$', 'object_detail', {'queryset': practice_areas, 'template_name':'practice_area_detail.html'}, "practice_details"),
)
