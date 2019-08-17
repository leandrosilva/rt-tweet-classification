import os
from sys_helpers import exit_if_error


def read_env(key):
    try:
        return os.environ[key]
    except Exception as e:
        exit_if_error(Exception("Environment variable '" + key + "' is missing."))


consumer_key = read_env("CONSUMER_KEY")
consumer_secret = read_env("CONSUMER_SECRET")
access_token = read_env("ACCESS_TOKEN")
access_token_secret = read_env("ACCESS_TOKEN_SECRET")
