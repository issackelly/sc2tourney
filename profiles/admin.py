from django.contrib import admin

from profiles.models import Player

class PlayerAdmin(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(Player, PlayerAdmin)
