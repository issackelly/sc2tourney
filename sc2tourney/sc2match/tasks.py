from sc2tourney.sc2match.models import Match, PlayerResult, Map
from sc2tourney.profiles.models import Player
from celery.task import task


def as_signal(sender, instance, created, raw):
    if created:
        parse_replay(instance.id)


@task
def parse_replay(match_id):
    match = Match.objects.get(match_id)

    match.players.all().delete()
    match.map = Map.objects.get_or_create(
        name=match.replay.map
    )


    for p in match.replay.players:
        player = Player.objects.get_or_create(
            username=p['name'],
            url=p['url']
        )
        result = None
        if p['result'] == 'Win':
            result = True
        elif p['result'] == 'Loss':
            result = False

        if p['pick_race'] == 'Random':
            random=True
        else:
            random=False

        PlayerResult.objects.create(
            match=match,
            player=player,
            result=result,
            random=random,
            color='rgb(%(r)s, %(g)s, %(b)s)' % p['color']
        )

    match.save()


