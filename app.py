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


@app.route('/tweets/<crypto>')
def get_crypto_tweets(crypto):
    try:
        query = f"{crypto} -filter:retweets"
        public_tweets = api.search(q=query, count=100, lang="en", tweet_mode='extended')
        tweets_data = [{'text': tweet.full_text, 'sentiment': TextBlob(tweet.full_text).sentiment.polarity} for tweet in public_tweets]
        return jsonify(tweets_data)
    except Exception as e:
        return jsonify({'error': str(e)})



if __name__ == '__main__':
    app.run(debug=True)
