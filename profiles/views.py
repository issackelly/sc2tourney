from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from profiles.models import Player


class PlayerView(DetailView):
    queryset = Player.objects.all()
    slug_field = 'username'
    slug_url_kwarg = 'username'

class PlayerList(ListView):
    queryset = Player.objects.all().order_by('username')
