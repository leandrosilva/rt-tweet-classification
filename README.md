# rt-tweet-classification

Simple pipeline for real-time text classification of tweets streamed from Twitter API.

There is a message producer that reads tweets, given one or more words to track, then streams them over Kafka so a consumer can proceed with the text classification. Using Kafka here makes it very easy to plug in additional steps in this pipeline or even serve different pipelines and stuff.

## Prerequisites

Before try it out, you got to provide a few Twitter API keys which you can find a place in `.env.sample`. And as you can see there, I suppose you would like to use `virtualenv` too. Sorry my presuntion though.

So our prerequisites here are:

* Python (https://www.python.org/)
* Virtualenv (https://virtualenv.pypa.io/)
* Apache Kafka (https://kafka.apache.org/)
* Twitter API (https://developer.twitter.com/)

As far as Kafka goes, if you have Docker installed, no worries, I got your back, a.k.a. `docker-compose.yml`.

When you are good to go with `python` and `virtualenv` installed and those Twitter keys on hand:

1. Open a terminal and `git clone` this repo wherever you like
2. Rename `.env.sample` to just `.env`
3. Add those Twitter keys on `.env`
4. Run `virtualenv .env` in the repo's root dir
5. Run `source .env` in the repo's root dir
5. Run `pip install -r requirements.txt`

Done.

## Try it out

First thing to do is to train the model. It is a one time kind of thing. So open a terminal and fire:

    $ source .env
    $ python trainer.py

Now, if you don't already have a Kafka up and running, you can use the provided `docker-compose.yml`:

    $ export DOCKERHOST=`docker-machine ip`
    $ docker-compose up -d

Once it is ready, you can start the `consumer` in one terminal:

    $ source .env
    $ python consumer.py

And finally, start the `producer` in another one:

    $ source .env
    $ python producer.py "Java" "PHP" "JavaScript"

Now you can stalk them all... ho ho ho
