from django.core.management.base import LabelCommand
from ...models import Tournament, Bracket, Round, Match


class Command(LabelCommand):
    def handle_label(self, label, **options):
        tournament = Tournament.objects.create(
            name=label
        )

        winners = Bracket.objects.create(
            tournament=tournament,
            name='Winners',
            order=0
        )
        losers = Bracket.objects.create(
            tournament=tournament,
            name='Losers',
            order=1
        )

        winners_round_1 = Round.objects.create(
            bracket=winners,
            name='Round 1',
            order=0
        )

        Match.objects.create(
            the_round=winners_round_1,
            order=0
        )
        Match.objects.create(
            the_round=winners_round_1,
            order=1
        )
        Match.objects.create(
            the_round=winners_round_1,
            order=2
        )
        Match.objects.create(
            the_round=winners_round_1,
            order=3
        )

        losers_round_1 = Round.objects.create(
            bracket=losers,
            name='Round 1',
            order=0
        )

        Match.objects.create(
            the_round=losers_round_1,
            order=0
        )
        Match.objects.create(
            the_round=losers_round_1,
            order=1
        )
        Match.objects.create(
            the_round=losers_round_1,
            order=2
        )
        Match.objects.create(
            the_round=losers_round_1,
            order=3
        )

        winners_round_2 = Round.objects.create(
            bracket=winners,
            name='Round 2',
            order=0
        )

        Match.objects.create(
            the_round=winners_round_2,
            order=0
        )
        Match.objects.create(
            the_round=winners_round_2,
            order=1
        )

        losers_round_2 = Round.objects.create(
            bracket=losers,
            name='Round 2',
            order=0
        )

        Match.objects.create(
            the_round=losers_round_2,
            order=0
        )
        Match.objects.create(
            the_round=losers_round_2,
            order=1
        )

        winners_round_3 = Round.objects.create(
            bracket=winners,
            name='Round 3',
            order=0
        )

        Match.objects.create(
            the_round=winners_round_3,
            order=0
        )

        losers_round_3 = Round.objects.create(
            bracket=losers,
            name='Round 3',
            order=0
        )

        Match.objects.create(
            the_round=losers_round_3,
            order=0
        )

        final_round = Round.objects.create(
            bracket=winners,
            name='Final',
            order=0
        )

        Match.objects.create(
            the_round=final_round,
            order=0
        )
