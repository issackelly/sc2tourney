from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone


class Player(models.Model):
    LEAGUES = (
        ('unranked', 'Unranked'),
        ('bronze', 'Bronze'),
        ('silver', 'Silver'),
        ('gold', 'Gold'),
        ('platinum', 'Platinum'),
        ('diamond', 'Diamond'),
        ('masters', 'Masters'),
        ('grandmasters', 'Grand Masters'),

    )

    player = models.ForeignKey(User, related_name='tournament_profile')
    tournament = models.ForeignKey('Tournament')
    seed = models.PositiveIntegerField(default=0)
    league = models.CharField(max_length=64, blank=True, default='', choices=LEAGUES)
    rank = models.IntegerField(blank=True, default=0, help_text='League ranking, not specific to the tournament.')

    class Meta:
        ordering = ['player']
        unique_together = []

    def __unicode__(self):
        return self.nickname

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nickname)

        return super(Player, self).save(*args, **kwargs)


class Tournament(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-start_date', 'name']

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super(Tournament, self).save(*args, **kwargs)


class Bracket(models.Model):
    tournament = models.ForeignKey(Tournament, related_name='brackets')
    name = models.CharField(max_length=64, help_text='Ex: Losers Bracket')
    slug = models.SlugField()
    order = models.PositiveIntegerField(default=0, help_text='Ordering within the tournament.')

    class Meta:
        ordering = ['tournament', 'order']
        unique_together = ['tournament', 'slug', 'order']

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super(Bracket, self).save(*args, **kwargs)


class Round(models.Model):
    bracket = models.ForeignKey(Bracket, related_name='rounds')
    name = models.CharField(max_length=64, help_text='Ex: Round A')
    slug = models.SlugField()
    order = models.PositiveIntegerField(default=0, help_text='Ordering within the tournament.')

    class Meta:
        ordering = ['bracket', 'slug', 'order']

    def __unicode__(self):
        return u"%s - %s" % (self.bracket, self.name)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super(Round, self).save(*args, **kwargs)



OUTCOMES = [
    ['win', 'Win'],
    ['tie', 'Tie'],
    ['forfeit', 'Forfeit'],
    ['unplayed', 'Unplayed'],
]


class Match(models.Model):
    the_round = models.ForeignKey(Round, related_name='matches')
    player_1 = models.ForeignKey(Player, related_name='matches_1')
    player_2 = models.ForeignKey(Player, related_name='matches_2')
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    order = models.PositiveIntegerField(default=0, help_text='Ordering within the round.')
    outcome = models.CharField(max_length=32, choices=OUTCOMES, default='unplayed')
    winner = models.ForeignKey(Player, related_name='matches_won', null=True, blank=True)
    player_1_score = models.CharField(max_length=32, blank=True, default='')
    player_2_score = models.CharField(max_length=32, blank=True, default='')
    notes = models.TextField(blank=True, default='')

    class Meta:
        verbose_name_plural = 'Matches'
        ordering = ['the_round', 'order']

    def __unicode__(self):
        return u"%s - %s vs. %s" % (self.the_round, self.player_1, self.player_2)

    def mark_outcome(self, outcome='win', player=None, score_1=None, score_2=None):
        self.outcome = outcome
        self.winner = player

        if score_1 is not None:
            self.player_1_score = score_1

        if score_2 is not None:
            self.player_2_score = score_2

        return self.save()

    def won(self, winner, score_1=None, score_2=None):
        return self.mark_outcome('win', winner, score_1, score_2)

    def tie(self, score_1=None, score_2=None):
        return self.mark_outcome('tie', None, score_1, score_2)

    def forfeit(self, winner):
        return self.mark_outcome('forfeit', winner)

    def unplayed(self):
        return self.mark_outcome('unplayed')


