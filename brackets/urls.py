from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('brackets.views',
    url(r'^(?P<tournament_slug>[\w\d._-]+)/$', 'tournament_detail', name='tournament_detail'),
    url(r'^(?P<tournament_slug>[\w\d._-]+)/b/(?P<bracket_slug>[\w\d._-]+)/$', 'bracket_detail', name='tournament_bracket_detail'),
    url(r'^(?P<tournament_slug>[\w\d._-]+)/b/(?P<bracket_slug>[\w\d._-]+)/r/(?P<round_slug>[\w\d._-]+)/$', 'round_detail', name='tournament_round_detail'),
    url(r'^(?P<tournament_slug>[\w\d._-]+)/b/(?P<bracket_slug>[\w\d._-]+)/r/(?P<round_slug>[\w\d._-]+)/m/r/(?P<match_pk>\d+)/$', 'match_detail', name='tournament_match_detail'),
    url(r'^(?P<tournament_slug>[\w\d._-]+)/b/(?P<bracket_slug>[\w\d._-]+)/r/(?P<round_slug>[\w\d._-]+)/m/r/(?P<match_pk>\d+)/upload_match/$', 'match_upload', name='tournament_match_upload'),

    url(r'^(?P<tournament_slug>[\w\d._-]+)/p/(?P<username>[\w\d._-]+)/$', 'player_detail', name='tournament_player_detail'),
)
