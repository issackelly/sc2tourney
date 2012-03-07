from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from sc2match.models import Match, PlayerResult, Map

class MatchView(DetailView):
    queryset = Match.objects.all()

class MatchList(ListView):
    queryset = Match.objects.all()
