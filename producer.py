from tweepy import OAuthHandler, Stream
from twitter_helpers import consumer_key, consumer_secret, access_token, access_token_secret
from sys_helpers import exit_if_error, wait_for_crl_c
from kafka_helpers import KAFKA_TWEET_TOPIC, get_kafka_hosts, create_kafka_producer, KafkaPusher
import time
import sys


DEFAULT_WORDS_TO_TRACK = ["Brazil", "Lula", "Bolsonaro", "Sérgio Moro", "Lava Jato", "Vaza Jato"]


def get_words_to_track():
    if len(sys.argv) == 1:
        return DEFAULT_WORDS_TO_TRACK
    words = sys.argv
    words.pop(0)
    return words


print("Authenticating on Twitter API...")
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


print("Connecting to produce Kafka records...")
producer, err = create_kafka_producer(KAFKA_TWEET_TOPIC, get_kafka_hosts())
exit_if_error(err)

pusher = KafkaPusher(KAFKA_TWEET_TOPIC, producer, print)


print("Ready to consume Twitter stream...")

WORDS_TO_TRACK = get_words_to_track()
print("Tracking words:", WORDS_TO_TRACK)

wait_for_crl_c()

stream = Stream(auth, pusher)
stream.filter(languages=["en"], track=WORDS_TO_TRACK, is_async=False)
