# Craigslist Scrap Bot Subscriptions

Subscribe to your own tailored craigslist scrap scraper and email bot. The bot
will monitor your local craigslist, and search for the variety of scrap metal
listings that you are interested in.

## How it Works

First, you sign up and configure some basics on the app or website:

- What kind of scrap are you looking for?
- How far are you willing to travel for scrap when you are available?

Then, install the mobile app, where you'll find a simple checkbox. You can
be available, or not available. When you are available, the bot will:

- Monitor your current location.
- Scrape craigslist for free scrap metal.
- Make contact with the listers, and send them a web form to quickly organize
  a pickup.

### Web Form for the Lister

The web form that the bot sends to the lister is designed to be simple and
easy to complete. The form will clearly dictate that the seller must be within
a range on the map for the subscriber to pickup, before they even begin to fill out
the form. However, if the seller is outside of range, the form will prompt the
seller to fill out the form anyway, and if the subscriber enters the area of
the pickup, it will notify the subscriber at that time.

### App Continues to Work After Form Submission

If the seller submits the form, it will be stored for five days. If the
subscriber, or any other subscriber for whom the listing applies, enters the
range of the seller, it will send the seller a quick email to confirm that
the scrap is still available, then send the pickup to the subscriber.

# TODO

- Write web forms and views
- Create REST api for app
