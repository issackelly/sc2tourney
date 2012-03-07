from registration.forms import RegistrationForm
from django import forms


class Sc2RegForm(RegistrationForm):
    username = forms.RegexField(regex=r'^[\w.@+-]+$',
                                max_length=30,
                                widget=forms.TextInput(attrs={'class': 'required'}),
                                label="Battle.net username",
                                error_messages={'invalid': "This value must contain only letters, numbers and underscores."})
    url = forms.URLField("Battle Net Profile URL", help_text="Go to http://us.battle.net/sc2/en/ and click on your avatar to go to your profile URL")
