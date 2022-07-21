import tweepy,re
from textblob import TextBlob
import matplotlib.pyplot as plt
import pandas as pd
class SentimentAnalysis:

    def __init__(self):
        self.twts = []
        self.tweetText = []

    def cleanTweet(self, tweet):
        tweet = re.sub('@[A-Za-z0-9]', '', tweet)
        tweet = re.sub('#', '', tweet)
        tweet = re.sub('RT[\s]+', '', tweet)
        tweet = re.sub('https?:\/\/\S+', '', tweet)
        return tweet

    def percentage(self, part, whole):
        temp = 100 * float(part) / float(whole)
        return format(temp, '.2f')

    def FetchTweets(self):
        consumerKey = 'BDNIfIxDTlItRHhJs0ywnmLlG'
        consumerSecret = 'MmnmcNaAk3LyQO3Xzw1HI0uEw1wKRqEa7eyoK1n4QXUtmKkj6T'
        accessToken = '1206921681454780417-4lHIVrR6IbUgbsYYkSbjV8LoowVlab'
        accessTokenSecret = 'SdVpmwDTkuEwXAbWHqsTZGAP6BfpPCknT91Yujs6wJ3P8'

        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        api = tweepy.API(auth)

        SearchTerm = input("Enter Keyword/Tag to search about: ")
        NOfTerms = int(input("Enter how many tweets to search: "))

        self.twts = tweepy.Cursor(api.search, q=SearchTerm, lang = "en").items(NOfTerms)

        polarity = 0
        positive = 0
        negative = 0
        neutral = 0

        for tweet in self.twts:
            self.tweetText.append(self.cleanTweet(tweet.text).encode('utf-8'))
            analysis = TextBlob(tweet.text)
            polarity += analysis.sentiment.polarity
            asp=analysis.sentiment.polarity

            if (asp == 0):
                neutral += 1

            elif (asp> 0 ):
                positive += 1

            elif (asp<0):
                negative += 1

        positive = self.percentage(positive, NOfTerms)

        negative = self.percentage(negative, NOfTerms)

        neutral = self.percentage(neutral, NOfTerms)

        print("How people are reacting on " + SearchTerm + " by analyzing " + str(NOfTerms) + " tweets.")
        print()
        print("Average Report: ")

        if (polarity == 0):
            print("Neutral")

        elif (polarity > 0):
            print("Positive")

        elif (polarity <0):
            print("Negative")


        print()
        print("Detailed Report: ")
        print(f"{positive}% people thought it was positive")

        print(f"{negative}% people thought it was negative")

        print(f"{neutral}% people thought it was neutral")
        labels = ['Positive', 'Negative', 'Neutral']
        vals = [positive, negative, neutral]
        plt.bar(vals, labels)
        plt.show()

sa = SentimentAnalysis()
sa.FetchTweets()