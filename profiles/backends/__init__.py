from registration.backends.default import DefaultBackend
from profiles.models import Player
from profiles.backends.forms import Sc2RegForm

class Sc2Backend(DefaultBackend):

    def register(self, request, **kwargs):
        user = super(Sc2Backend, self).register(request, **kwargs)
        player, created = Player.objects.get_or_create(
            username=user.username,
        )
        player.user = user
        if not player.battle_net_url:
            player.battle_net_url = kwargs['bnet_url']
        player.save()

    def get_form_class(self):
        print 'derp'
        return Sc2RegForm

