from django.db import models
from profiles.models import Player

import sc2reader
from django.utils import timezone



class PlayerResult(models.Model):
    RACES = (
        ("terran", "Terran"),
        ("protoss", "Protoss"),
        ("zerg", "Zerg")
    )

    player = models.ForeignKey(Player, related_name="matches")
    match = models.ForeignKey('Match', related_name="players")
    result = models.NullBooleanField(default=None)
    color = models.CharField(max_length=32)
    random = models.BooleanField(default=False)
    race = models.CharField(choices=RACES, max_length=8)

    @property
    def race_letter(self):
        if self.race:
            return self.race[0].upper()
        return '-'

class Map(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to="maps", blank=True, null=True)
    map_file = models.FileField(upload_to="map_files", blank=True, null=True)

    def __unicode__(self):
        return self.name


class Match(models.Model):
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(editable=False)
    replay_file = models.FileField(upload_to="replay_files/%Y/%m/%d")
    mapfield = models.ForeignKey(Map, null=True, editable=False)
    duration = models.PositiveIntegerField(null=True, editable=False)
    gateway = models.CharField(max_length=32, default="us")

    def __init__(self, *args, **kwargs):
        self._replay = None
        super(Match, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return "(%s) over (%s) on %s in %s" % (
            ", ".join(["%s[%s]" % (p.player.username, p.race_letter) for p in self.winners]),
            ", ".join(["%s[%s]" % (p.player.username, p.race_letter) for p in self.losers]),
            self.mapfield,
            self.time_display
        )

    @property
    def replay(self):
        if not self._replay:
            self._replay = sc2reader.load_replay(self.replay_file.file)
        return self._replay

    @property
    def time_display(self):
        if self.duration:
            minutes = self.duration / 60
            seconds = self.duration % 60
            if seconds < 10:
                seconds = "0%s" % seconds
            return '%s:%s' % (minutes, seconds)
        else:
            return '-'


    @property
    def winners(self):
        return self.players.filter(result=True)

    @property
    def losers(self):
        return self.players.filter(result=False)


    def save(self, *args, **kwargs):
        self.modified = timezone.now()
        super(Match, self).save(*args, **kwargs)
