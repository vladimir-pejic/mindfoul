from django.shortcuts import render
from django.conf import settings
import tweepy
from textblob import TextBlob


def index(request):
    auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
    auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_SECRET)

    api = tweepy.API(auth)

    stats = []
    tweets = api.user_timeline()
    # tweets = api.home_timeline()

    if request.method == 'POST':
        responses = api.search(request.POST['word'])
        for response in responses:
            analysis = TextBlob(response.text)
            analysis_dict = {'tags': analysis.tags, 'sentiment': analysis.sentiment}
            stats.append(analysis_dict)

    context = {'stats': stats, 'tweets': tweets}

    return render(request, 'tweetalize/index.html', context);