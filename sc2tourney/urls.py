from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import Http404
from django.template.response import TemplateResponse
from django.views.generic.simple import direct_to_template

admin.autodiscover()


def direct(request, path):
    try:
        return TemplateResponse(request, "%s.html" % path[:-1], {})
    except:
        raise Http404


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', direct_to_template, {"template": "homepage.html"}, name="home"),
)

urlpatterns += staticfiles_urlpatterns()

urlpatterns += patterns('',
    url(r"(?P<path>.*)", direct)
)


from sc2tourney.sc2match.tasks import as_signal
from sc2tourney.sc2match.models import Match
from django.db.models import post_save
post_save.connect(Match, as_signal)
