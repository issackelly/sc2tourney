from django.forms import ModelForm
from sc2match.models import Match


class MatchUpload(ModelForm):

    class Meta:
        model = Match
        fields = ['replay_file']

