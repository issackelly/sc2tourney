from django.contrib import admin
from sc2tourney.sc2match.models import Match, PlayerResult

class MatchAdmin(admin.ModelAdmin):
    list_display = ['id']

class PlayerResultAdmin(admin.ModelAdmin):
    list_display = ['player', 'match']



admin.site.register(PlayerResult, PlayerResultAdmin)
admin.site.register(Match, MatchAdmin)
