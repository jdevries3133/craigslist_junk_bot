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
        for i in range(100):
            i += 1
            data = {
                "query": get_random_string(i),
                "pickup_range": i,
                "blacklist_words": '\n'.join([get_random_string(i % 20) for _ in range(i % 5)]),
                "greylist_phrases": '\n'.join([(get_random_string(i % 20) * (i % 8)) for _ in range(i % 5)]),
                "qset_threshold": i,
            }
            form = ProfileSetupForm(data)
            if len(data['query']) > 50:
                assert not form.is_valid()
            elif 45 <= data['qset_threshold'] <= 65:
                assert form.is_valid()
            else:
                assert not form.is_valid()
                continue

            # test form save method
            form.save(User.objects.get(username='test'))
            created_profile = SubscriberProfile.objects.get(user=self.user)
            created_blacklist = BlacklistWord.objects.get(user=self.user)
            created_greylist = GreylistPhrase.objects.get(user=self.user)
            assert created_profile.query == data['query']
            assert created_profile.pickup_range == data['pickup_range']
            assert created_blacklist.blacklist_words == data['blacklist_words']
            assert created_greylist.greylist_words == data['greylist_words']
            assert created_greylist.qset_threshold == data['qset_threshold']
            
            
            