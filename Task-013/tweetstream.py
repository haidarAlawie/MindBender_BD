from kafka import KafkaProducer
from datetime import datetime
import tweepy
import sys
import re

# topics that stream will look for
TWEET_TOPICS = ['Lebanon']

KAFKA_BROKER = 'localhost:9099'
KAFKA_TOPIC = 'tweets'

class Streamer(tweepy.StreamListener):

    def on_error(self, status_code):
        if status_code == 402:
            return False

    def on_status(self, status):

        tweet = status.text
        # get rid of links and retweets
        tweet = re.sub(r'RT\s@\w*:\s', '', tweet)
        tweet = re.sub(r'https?.*', '', tweet)
        # encoding 
        global producer
        producer.send(KAFKA_TOPIC, bytes(tweet, encoding='utf-8'))

        d = datetime.now()

        print(f'[{d.hour}:{d.minute}.{d.second}] sending tweet')

# put your API keys here
consumer_key = 'gO4hC6cP1G1xUf8fhrR4PzXWo'
consumer_secret_key = 'hrB7g9Rctuc5AMFdvg6abOHZhBab1xDYvygV412DD4oBNN6TjQ'

access_token = '1322199969911230467-mXXNwPrENcfykwxPqoAWzdbviXnKhx'
access_token_secret = 'yhHKBQPXqswk17iyJE8FSMmnt1jQRiv65MzgxKplGPUst'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

streamer = Streamer()
stream = tweepy.Stream(auth=api.auth, listener=streamer)

try:
    producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER)
except Exception as e:
    print(f'Error Connecting to Kafka --> {e}')
    sys.exit(1)

stream.filter(track=TWEET_TOPICS)
