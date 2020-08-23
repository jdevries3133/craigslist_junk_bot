import re
import ssl

from fuzzywuzzy import fuzz
import feedparser


class RssProcessor:
    def __init__(
        self,
        blacklist_words=None,
        grey_phrases=None,
        qset_threshold=60,
        rss_uri=None,
        feed=None
    ):
        # fix ssl issue
        if hasattr(ssl, '_create_unverified_context'):
            ssl._create_default_https_context = ssl._create_unverified_context
        self.feed = feed if feed else feedparser.parse(rss_uri)
        self.blacklist_words = blacklist_words if blacklist_words else []
        self.grey_phrases = grey_phrases if grey_phrases else []
        self.qset_threshold = qset_threshold

    def get_listings(self):
        if not 'listings' in self.__dict__:
            self.listings = []
        for post in self.feed['entries']:
            self._process_post(post)
        return self.listings

    def _process_post(self, post):
        """
        Checks post against black and grey words.
        Appends post to self.listings only if it is passes the filter.
        Returns True if the post was added or False if not.
        """
        processed_summary = re.split(re.compile(r';|\.|,|\n|!|\?'), post['summary'])
        for snippet in processed_summary:
            snippet = snippet.strip()
            if not snippet:
                continue
            for i in snippet.split(' '):
                if i.strip().lower() in self.blacklist_words:
                    return False
            for bad_phrase in self.grey_phrases:
                ratio = fuzz.ratio(snippet, bad_phrase)
                if ratio > 60:
                    print(
                        'ELIMINATED BY PHRASE MATCH:',  '\n',
                        'bad',      '\t', bad_phrase,   '\n',
                        'phr',      '\t', snippet,      '\n',
                        'ratio',    '\t', ratio,        '\n',
                    )
                    return False
        self.listings.append(post)
    
    def _print(self):
        if not self.listings:
            for post in self.feed['entries']:
                print('-' * 80)
                for word in post['title'].split(' '):
                    if word in self.blacklist_words:
                        continue
                for k, v in post.items():
                    print('(', k, ')', v, '\n')
                input('PRESS ENTER FOR NEXT LISTING')
        else:
            for post in listings:
                print('-' * 80)
                for word in post['title'].split(' '):
                    if word in self.blacklist_words:
                        continue
                for k, v in post.items():
                    print('(', k, ')', v, '\n')
                input('PRESS ENTER FOR NEXT LISTING')

if __name__ == '__main__':
    bl_words = [
        'electronic'
    ]
    bl_phrase = [
        'I will pickup scrap',
        'We buy cars for cash'
    ]
    rss_uri = 'https://newjersey.craigslist.org/search/sss?format=rss&query=scrap+metal'
    feed = RssProcessor(
        blacklist_words=bl_words,
        grey_phrases=bl_phrase,
        rss_uri=rss_uri
    )
    listings = feed.get_listings()
    breakpoint()
