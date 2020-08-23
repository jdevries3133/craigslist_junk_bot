import re
import ssl

from fuzzywuzzy import fuzz
import feedparser


class RssProcessor:
    def __init__(self, blacklist_words=None, blacklist_phrases=None, debug=False):
        # fix ssl issue
        if hasattr(ssl, '_create_unverified_context'):
            ssl._create_default_https_context = ssl._create_unverified_context
        self.feed = feedparser.parse('https://newjersey.craigslist.org/search/sss?format=rss&query=scrap+metal')
        self.listings = []  # is appended to by self.process(), which filters undesirable posts
        # checked for exact match
        self.blacklist_words = [
            'computer',
            'electronic',
        ]
        if blacklist_words:
            self.blacklist_words += blacklist_words
        # checked for a nearmatch with fuzzy pattern matching
        self.blacklist_phrases = [
            'I can pick up scrap metal',
        ]
        if blacklist_phrases:
            self.blacklist_phrases += blacklist_phrases
        self.debug = debug

    def process(self):
        '''
        Mutates self.feed to remove undesirable posts
        '''
        for post in self.feed['entries']:
            processed_summary = re.split(re.compile(r';|\.|,|\n|!|\?'), post['summary'])
            # try to further split run-on sentences
            for snippet in processed_summary:
                snippet = snippet.strip()
                if not snippet and snippet != '\n':  # if the snippet is blank, continue
                    continue
                for i in snippet.split(' '):
                    if i.strip().lower() in self.blacklist_words:
                        continue
                for bad_phrase in self.blacklist_phrases:
                    ratio = fuzz.ratio(snippet, bad_phrase)
                    if ratio > 60:
                        print('ELIMINATED BY PHRASE MATCH:')
                        print('bad', '\t', bad_phrase)
                        print('phr', '\t', snippet)
                        print('ratio', '\t', ratio)
                        if self.debug:
                            inp = input('Would you like to eliminate? (y/n)').lower()
                            while True:
                                if inp == 'y':
                                    break
                                if inp == 'n':
                                    break
                                else:
                                    inp = input('Enter y or n').lower()
                            if inp == 'y':
                                continue
                        else:
                            continue
            # at this point, we know the post is good
            listing = Listing(post)
            self.listings.append(listing)
    
    def _print(self):
        for post in self.feed['entries']:
            print('-' * 80)
            for word in post['title'].split(' '):
                if word in self.blacklist_words:
                    continue
            for k, v in post.items():
                print('(', k, ')', v, '\n')
            input()

class Listing:
    def __init__(self, rss_obj):
        self.source_cached = False
        self.rss_obj = rss_obj
        self.rough_location = rss_obj['dc_source'].split('-')[-2]


if __name__ == '__main__':
    feed = RssProcessor(debug=True)
    feed.process()
