import tweepy
from time import sleep


consumer_key = 'YOUR_KEY'
consumer_secret = 'YOUR_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_TOKEN_SECRET'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

person = api.user_timeline(screenname = 'Curry2615')

public_tweets = api.home_timeline()

test = [
    "potato",
    "pie",
    "1+1+1"
]
# my_file=open('sample20.txt','r')
# file_lines=my_file.readlines()
# my_file.close()



# for line in test:
# # Add try ... except block to catch and output errors
#     try:
#         print(line)
#         if line != '\n':
#             #this line tweets the input
#             api.send_direct_message(person)
#         else:
#             pass
#     except tweepy.TweepError as e:
#         print(e.reason)
#     sleep(5)

for tweet in tweepy.Cursor(api.search, q='#Salah').items():
    try:
        # Add \n escape character to print() to organize tweets
        print('\nTweet by: @' + tweet.user.screen_name)

        # Retweet tweets as they are found
        tweet.retweet()
        print('Retweeted the tweet')

        sleep(5)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
