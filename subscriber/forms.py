from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from .models import SubscriberProfile, BlacklistWord, GreylistPhrase


class SubscriberProfileForm(forms.Form):
    query = forms.CharField(label="Your Search Query", max_length=50)
    pickup_label = "How far are you willing to travel to pickup scrap?"
    pickup_range = forms.IntegerField(label=pickup_label), required=False)

class BlacklistWordForm(forms.ModelForm):
    class Meta:
        model = BlacklistWord
        fields = ('word',)

class GreylistPhraseForm(forms.ModelForm):
    class Meta:
        model = GreylistPhrase
        fields = ('phrase', 'qset_threshold')