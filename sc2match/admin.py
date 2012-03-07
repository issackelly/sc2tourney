from django.contrib import admin
from .models import Match, PlayerResult

class MatchAdmin(admin.ModelAdmin):
    list_display = ['id']
    readonly_fields = [
        'mapfield',
        'duration',
    ]

class PlayerResultAdmin(admin.ModelAdmin):
    list_display = ['player', 'match']



admin.site.register(PlayerResult, PlayerResultAdmin)
admin.site.register(Match, MatchAdmin)
