from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
import pickle
from pathlib import Path


# The 20 Newsgroups data set is a collection of approximately 20,000 newsgroup documents,
# partitioned (nearly) evenly across 20 different newsgroups.
# http://qwone.com/~jason/20Newsgroups/
DEFAULT_CATEGORIES = ["talk.politics.misc", "misc.forsale", "rec.motorcycles",
                      "comp.sys.mac.hardware", "sci.med", "talk.religion.misc"]


def fetch_train_dataset(categories):
    train_dataset = fetch_20newsgroups(subset="train", categories=categories, shuffle=True, random_state=42)
    return train_dataset


def bag_of_words(categories, save=False):
    count_vect = CountVectorizer()
    X_train_counts = count_vect.fit_transform(fetch_train_dataset(categories).data)
    if save:
        pickle.dump(count_vect.vocabulary_, open_vocab_for_write())
    return X_train_counts


def tf_idf(categories):
    tf_transformer = TfidfTransformer()
    return (tf_transformer, tf_transformer.fit_transform(bag_of_words(categories, True)))


def model(categories, save=False):
    classifier = MultinomialNB().fit(tf_idf(categories)[1], fetch_train_dataset(categories).target)
    if save:
        pickle.dump(classifier, open_model_for_write())
    return classifier


# Utility functions

def open_vocab_for_write():
    may_create_models_dir()
    return open("models/vocabulary.pickle", "wb")


def load_vocabulary():
    try:
        return pickle.load(open("models/vocabulary.pickle", "rb")), None
    except Exception as e:
        return None, e


def open_model_for_write():
    may_create_models_dir()
    return open("models/model.pickle", "wb")


def load_model():
    try:
        return pickle.load(open("models/model.pickle", "rb")), None
    except Exception as e:
        return None, e


def may_create_models_dir():
    models_dir = Path("models/")
    if not models_dir.exists():
        models_dir.mkdir()
