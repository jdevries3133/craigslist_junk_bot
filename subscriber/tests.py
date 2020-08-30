from random import random
from django.test import TestCase
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from .forms import ProfileSetupForm
from .models import SubscriberProfile, BlacklistWord, GreylistPhrase

# Create your tests here.
class TestForms(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="test",
            password="test",
        )

    def test_profile_setup_form_basic_validation(self):
        for i in range(300):
            i += 1
            gen_words = [get_random_string(i % 20) for _ in range(i % 5)]
            gen_phrases = [(get_random_string(i % 20) * ((i % 8) + 1)) for _ in range(i % 5)]
            data = {
                "query": get_random_string(i % 53),
                "pickup_range": i % 20,
                "blacklist_words": '\n'.join(gen_words),
                "greylist_phrases": '\n'.join(gen_phrases),
                "qset_threshold": i % 70,
            }
            if random() < 0.04:
                data['blacklist_words'] == '\n\n\n\nn\nn\n\n\n\n\nnn'
                data['greylist_phrases'] == '\n\\n\n\n\n\nn\n\nn\n\n\n'
            form = ProfileSetupForm(data)
            if len(data['query']) > 50:
                assert not form.is_valid()
                continue
            elif 45 <= data['qset_threshold'] <= 65:
                assert form.is_valid()
            else:
                assert not form.is_valid()
                continue
            # test form save method
            form.save(User.objects.get(username='test'))
            created_profile = SubscriberProfile.objects.get(user=self.user)
            created_blacklists = BlacklistWord.objects.filter(subscriber=created_profile)
            created_greylists = GreylistPhrase.objects.filter(subscriber=created_profile)
            if 'query' in data:
                assert created_profile.query == data['query']
            if 'pickup_range' in data:
                assert created_profile.pickup_range == data['pickup_range']
            words = [i for i in data['blacklist_words'].split('\n') if i != '']
            for w in words:
                assert BlacklistWord.objects.filter(word=w)
            assert len(created_blacklists) == len(words)
            phrases = [i for i in data['greylist_phrases'].split('\n') if i != '']
            for p in phrases:
                assert GreylistPhrase.objects.filter(phrase=p)
            assert len(created_blacklists) == len(phrases)
            
            created_profile.delete()  # one to one field
            assert not BlacklistWord.objects.all()
            assert not GreylistPhrase.objects.all()