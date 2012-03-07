from django.contrib import admin
from .models import Player, Tournament, Bracket, Round, Match


class PlayerAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['nickname'],
    }


class TournamentAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['name'],
    }


class BracketAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['name'],
    }


class RoundAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['name'],
    }


class MatchAdmin(admin.ModelAdmin):
    pass


admin.site.register(Player, PlayerAdmin)
admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Bracket, BracketAdmin)
admin.site.register(Round, RoundAdmin)
admin.site.register(Match, MatchAdmin)
