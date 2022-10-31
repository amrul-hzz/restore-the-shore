from django.forms import ModelForm
from leaderboard.models import LeaderBoard

class AccountForm(ModelForm):
    class Meta:
        model = LeaderBoard
        fields = ['quote']