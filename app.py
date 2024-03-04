import tweepy
from dotenv import load_dotenv
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

if __name__ == '__main__':
    app.run(debug=True)
