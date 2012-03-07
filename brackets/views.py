from django.shortcuts import get_object_or_404, render
from .models import Player, Tournament, Bracket, Round, Match


def tournament_detail(request, tournament_slug):
    all_tournaments = Tournament.objects.all().select_related(depth=4)
    tournament = get_object_or_404(all_tournaments, slug=tournament_slug)
    return render(request, 'brackets/tournament_detail.html', {
        'tournament': tournament,
    })


def bracket_detail(request, tournament_slug, bracket_slug):
    tournament = get_object_or_404(Tournament, slug=tournament_slug)
    bracket = get_object_or_404(tournament.brackets.all(), slug=bracket_slug)
    return render(request, 'brackets/bracket_detail.html', {
        'tournament': tournament,
        'bracket': bracket,
    })


def round_detail(request, tournament_slug, bracket_slug, round_slug):
    tournament = get_object_or_404(Tournament, slug=tournament_slug)
    bracket = get_object_or_404(tournament.brackets.all(), slug=bracket_slug)
    the_round = get_object_or_404(bracket.rounds.all(), slug=round_slug)
    return render(request, 'brackets/round_detail.html', {
        'tournament': tournament,
        'bracket': bracket,
        'round': the_round,
    })


def match_detail(request, tournament_slug, bracket_slug, round_slug, match_pk):
    tournament = get_object_or_404(Tournament, slug=tournament_slug)
    bracket = get_object_or_404(tournament.brackets.all(), slug=bracket_slug)
    the_round = get_object_or_404(bracket.rounds.all(), slug=round_slug)
    match = get_object_or_404(the_round.matches.all(), pk=match_pk)
    return render(request, 'brackets/match_detail.html', {
        'tournament': tournament,
        'bracket': bracket,
        'round': the_round,
        'match': match,
    })


def player_detail(request, tournament_slug, player_slug):
    tournament = get_object_or_404(Tournament, slug=tournament_slug)
    player = get_object_or_404(Player, tournament__slug=tournament_slug, slug=player_slug)
    return render(request, 'brackets/player_detail.html', {
        'tournament': tournament,
        'player': player,
    })
