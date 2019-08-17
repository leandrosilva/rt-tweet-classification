# rt-tweet-classification

Simple pipeline for real-time text classification of tweets streamed from Twitter API.

There is a message producer that reads tweets, given one or more words to track, then streams them over Kafka so a consumer can proceed with the text classification. The use of Kafka here makes it very easy to plug in additional steps in this pipeline or even serve different pipelines and stuff.

## Prerequisites

Before try it out, you got to provide a few Twitter API parameters which you can find a place in `.env.sample`. And as you can see there, I suppose you would like to use `virtualenv` too. Sorry my presuntion though.

* Twitter API (https://developer.twitter.com/)
* Virtualenv (https://virtualenv.pypa.io/)

When you are good to go with `virtualenv` installed and keys on hand:

1. Open a terminal and `git clone` this repo wherever you like
2. Rename `.env.sample` to just `.env`
3. Add those Twitter keys on `.env`
4. Run `virtualenv .env` in the repo's root dir
5. Run `source .env` in the repo's root dir
5. Run `pip install -r requirements.txt`

## Try it out

If you don't already have a Kafka up and running, you can use the provided `docker-compose.yml`:

    $ docker-compose up -d

Once it is ready, you can start the `consumer`.

    $ source .env
    $ python consumer.py

And finally, start the `producer`:

    $ source .env
    $ python producer.py "Java" "PHP" "JavaScript"

Now you can stalk them all... ho ho ho
