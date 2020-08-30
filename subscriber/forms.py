from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from .models import SubscriberProfile, BlacklistWord, GreylistPhrase


class NewlineDelimitedTextArea(forms.CharField):
    def to_python(self, value):
        if not value:
            return []
        return value.split('\n')
        

class ProfileSetupForm(forms.Form):
    query = forms.CharField(
        help_text=(
            'In Craigslist, this is the exact query that will be searched for, '
            'within the "for free" section. It is recommended to keep the default '
            'querystring of "scrap metal," but if you do customize your querystring, '
            'keep it as vague as possible to avoid limiting your results.'
        ),
        label="Your Craigslist Search Query",
        max_length=50,
        required=False,
        initial="scrap metal"
    )
    pickup_range = forms.IntegerField(
        help_text=(
            'In miles, how far would you like to go out of your way for scrap. '
            'Keep in mind, this is relative to your current location at the time '
            'the bot engages with the lister.'
        ),
        required=True,
        initial=8
    )
    blacklist_words = NewlineDelimitedTextArea(
        widget=forms.Textarea,
        help_text=(
            'Input a list of words, one on each line, that you would like to '
            'comprise your blacklist. If any of these words appear in the listing '
            'title or description, the listing will be ignored.\n\nFor example, '
            'you might want to avoid electronic scrap with the blacklist above. '
        ),
        initial="electronic\ne-waste\ncomputer",
        label="Blacklist Words",
        required=False
    )
    greylist_phrases = NewlineDelimitedTextArea(
        widget=forms.Textarea,
        help_text=(
            'These are phrases that you want the algorithm to try to avoid. '
            'For example, there are a lot of "I can come pickup scrap," type '
            'positngs on craigslist. You probably want to avoid these by using '
            'the default blacklist above.'
        ),
        initial="I can pick up scrap\nI will pick up scrap",
        required=False
    )
    qset_threshold = forms.IntegerField(
        help_text=(
            'You may set this value between 45 and 65. The lower the number, the '
            'more aggressive the phrase matching algorithm will be, and the more '
            'listings it will eliminate. The higher the number, the more picky '
            'the algorithm will be, and it will only eliminate listings that '
            'match your phrases very closely.'
        ),
        required=False,
        initial=60,
        label="Greylist Phrases",
        validators=[MinValueValidator(45), MaxValueValidator(65)]
    )

    def save(self, user):
        data = self.cleaned_data
        subscriber = SubscriberProfile.objects.create(
            user=user,
            query=(data['query'] if 'query' in data else 'scrap metal'),
            pickup_range=(data['pickup_range'] if 'pickup_range' in data else 8),
            is_profile_setup=True
        )
        for word in data['blacklist_words']:
            BlacklistWord.objects.create(
                subscriber=subscriber,
                word=word
            )
        for phrase in data['greylist_phrases']:
            GreylistPhrase.objects.create(
                subscriber=subscriber,
                phrase=phrase,
                qset_threshold=data['qset_threshold']
            )

