from django.db import models
from profiles.models import Player

from sc2reader.resources import Replay
from django.utils import timezone



class PlayerResult(models.Model):
    RACES = (
        ("terran", "Terran"),
        ("protoss", "Protoss"),
        ("zerg", "Zerg")
    )

    player = models.ForeignKey(Player)
    match = models.ForeignKey('Match')
    result = models.NullBooleanField(default=None)
    color = models.CharField(max_length=32)
    random = models.BooleanField(default=False)
    race = models.CharField(choices=RACES, max_length=8)


class Map(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to="maps", blank=True, null=True)
    map_file = models.FileField(upload_to="map_files", blank=True, null=True)


class Match(models.Model):
    players = models.ManyToManyField(Player, through=PlayerResult)

    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(editable=False)
    replay_file = models.FileField(upload_to="replay_files/%Y/%m/%d")
    mapfield = models.ForeignKey(Map, null=True)
    duration = models.PositiveIntegerField(null=True)

    def __init__(self, *args, **kwargs):
        self._replay = None
        super(Match, self).__init__(*args, **kwargs)

    @property
    def replay(self):
        if not self._replay:
            try:
                self._replay = Replay(self.replay_file.open())
            except IOError:
                return None
        return self._replay


    @property
    def winner(self):
        winner = None
        try:
            winner = self.players.filter(result=True)[0]
        except IndexError:
            pass
        return winner

    @property
    def loser(self):
        loser = None
        try:
            loser = self.players.filter(result=False)[0]
        except IndexError:
            pass
        return loser

    def save(self, *args, **kwargs):
        self.modified = timezone.now()
        super(Match, self).save(*args, **kwargs)
