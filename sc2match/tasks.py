from sc2match.models import PlayerResult, Map, Match
from profiles.models import Player
from celery.task import task


def as_signal(sender, instance, created, raw, **kwargs):
    if created:
        parse_replay.delay(instance.id)

@task
def parse_replay(match_id):
    match = Match.objects.get(id=match_id)
    match.players.all().delete()
    match.mapfield, created = Map.objects.get_or_create(
        name=match.replay.map_name,
    )
    match.duration = match.replay.game_length.seconds
    match.gateway = match.replay.gateway

    for p in match.replay.players:
        player, created = Player.objects.get_or_create(
            username=p.name,
            battle_net_url=p.url
        )
        result = None
        if p.result == 'Win':
            result = True
        elif p.result == 'Loss':
            result = False

        if p.pick_race == 'Random':
            random=True
        else:
            random=False

        PlayerResult.objects.create(
            match=match,
            player=player,
            result=result,
            random=random,
            color='rgb(%(r)s, %(g)s, %(b)s)' % p.color,
            race=p.play_race,
        )

    match.save()


