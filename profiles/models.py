from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    user = models.OneToOneField(User, null=True)
    username = models.CharField(max_length=64, unique=True)
    battle_net_url = models.URLField(help_text="Go to http://us.battle.net/sc2/en/ and click on your avatar to go to your profile URL", blank=True)

    def __unicode__(self):
        return self.username
