import os
from urllib import parse
from kafka import KafkaConsumer, KafkaProducer
from tweepy.streaming import StreamListener
import json


KAFKA_TWEET_TOPIC = "twitter-stream"


def get_kafka_hosts():
    try:
        docker_host = parse.urlsplit(os.environ["DOCKER_HOST"]).netloc.split(":")[0]
        return [docker_host + ":29092"]
    except:
        return ["localhost:29092"]


def create_kafka_consumer(topic, broker_list):
    try:
        return (KafkaConsumer(topic, bootstrap_servers=broker_list), None)
    except Exception as e:
        return (None, e)


def create_kafka_producer(topic, broker_list):
    try:
        return (KafkaProducer(bootstrap_servers=broker_list), None)
    except Exception as e:
        return (None, e)


class KafkaPusher(StreamListener):
    def __init__(self, topic, producer, logger):
        self.topic = topic
        self.producer = producer
        self.logger = logger

    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
        self.logger("[PUSHING TWEET] =>", tweet)
        self.producer.send(self.topic, value=tweet.encode('utf-8'))
        return True

    def on_error(self, status):
        self.logger("Error:", status)
        return True
