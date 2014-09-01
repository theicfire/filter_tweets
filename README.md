How to use:

1) Make a secrets.json file containing
    - consumer_key
    - consumer_secret
    - authorization_key
    - authorization_secret
Ex:

{
    "consumer_key": "XXX",
    "consumer_secret": "XXX",
    "access_token": "XXX",
    "access_token_secret": "XXX"
}

For more information on how to get these, visit dev.twitter.com

2) Install the python dependencies
$ pip install -r requirements.txt

3) Run the python file, to get tweets that are not retweeted or conversations
$ python filtered_tweets.py katyperry --refetch
To get a local copy of the tweets, run this without the "--refetch" flag