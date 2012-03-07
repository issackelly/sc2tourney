from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import direct_to_template

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', direct_to_template, {"template": "homepage.html"}, name="home"),
    url(r'^t/', include('brackets.urls')),
)

urlpatterns += staticfiles_urlpatterns()


from sc2match.tasks import as_signal
from sc2match.models import Match
from django.db.models.signals import post_save
post_save.connect(as_signal, Match)
