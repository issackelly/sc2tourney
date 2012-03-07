from django.conf.urls.defaults import patterns, url
from sc2match.views import MatchView, MatchList

urlpatterns = patterns('sc2match.views',
    url(r'^match/$', MatchList.as_view(), name='match_list'),
    url(r'^match/(?P<pk>[\d]+)/$', MatchView.as_view(), name='match_detail'),
)
