import game
from http.server import BaseHTTPRequestHandler
from dotenv import load_dotenv
import tweepy
import os

# Allows for searching of a `.env` file that holds environment variables
load_dotenv()

# TODO probably ignore this handler stuff. there are better ways to handle this
class handler():
    def do_GET(self):
        # Set up Tweepy and authenticate with the Twitter API
        consumer_key = os.getenv('CONSUMER_KEY')
        consumer_secret = os.getenv('CONSUMER_SECRET')
        access_token = os.getenv('ACCESS_TOKEN')
        access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')


        # Do the actual auth stuff and get that from tweepy docs    
        # auth = tweepy.O
        # auth.set_access_token

        # client = tweepy.client ? I think anyway

        # Insert tictactoe game logic here

        # Then insert tweepy specific stuff
        return


if __name__=="__main__":
    weiner = handler()
    weiner.do_GET()
