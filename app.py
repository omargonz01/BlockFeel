import tweepy
from dotenv import load_dotenv
from textblob import TextBlob
import os
from flask import Flask, jsonify

app = Flask(__name__)

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/tweets')
def get_tweets():
    public_tweets = api.home_timeline()
    tweets = [tweet.text for tweet in public_tweets]
    return jsonify(tweets)


@app.route('/tweets/<crypto>')
def get_tweets(crypto):
    public_tweets = api.search(q=crypto, count=100, lang="en")
    tweets = [tweet.text for tweet in public_tweets]
    return jsonify(tweets)


@app.route('/tweets/<crypto>')
def get_crypto_tweets(crypto):
    public_tweets = api.search(q=crypto, count=100, lang="en")
    tweets_data = []
    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)
        sentiment = analysis.sentiment.polarity
        tweets_data.append({'text': tweet.text, 'sentiment': sentiment})
    return jsonify(tweets_data)


if __name__ == '__main__':
    app.run(debug=True)
