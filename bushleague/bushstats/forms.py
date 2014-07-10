from django import forms
from bushstats.models import Player

class PlayerForm(forms.ModelForm):
	name = forms.CharField(max_length=128, help_text="help_text")
	wins = models.IntegerField(initial=0)
        loses = models.IntegerField(default=0)
        kills = models.IntegerField(default=0)
        deaths = models.IntegerField(default=0)
        gpm = models.IntegerField(default=0)
        bkbtiming = models.TimeField(auto_now=False, auto_now_add=False, default="00:00")
