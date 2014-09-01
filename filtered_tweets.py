import tweepy
import json
import pickle
import argparse


# Authentication details. To  obtain these visit dev.twitter.com and store in secrets.json
with open('secrets.json', 'r') as f:
    secrets = json.load(f)

def get_tweets(username, count=500):
    auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
    auth.set_access_token(secrets['access_token'], secrets['access_token_secret'])
    api = tweepy.API(auth)
    with open('pickled_{}.txt'.format(username), 'w') as f:
        timeline = api.user_timeline(username, count=count)
        f.write(pickle.dumps(timeline))


def read_file(username):
    with open('pickled_{}.txt'.format(username), 'r') as f:
        return pickle.load(f)


def print_from_timeline(timeline):
    for i, tweet in enumerate(timeline):
        print i, ':', tweet.text, str(tweet.created_at)


def filter_tweet(tweet):
    # filter RTs and @ reply tweets
    return not any([
        tweet.text.startswith('@'),
        tweet.text.startswith('RT')
        ])


def filtered_tweets(username):
    return filter(filter_tweet, read_file(username))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    parser.add_argument('username')
    parser.add_argument('--refetch', action='store_true', dest='refetch')
    args = parser.parse_args()

    if getattr(args, 'refetch', False):
        get_tweets(args.username)
    print_from_timeline(filtered_tweets(args.username))


