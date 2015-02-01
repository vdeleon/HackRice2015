#CREATES A STREAM TO LISTEN TO TWEETS ABOUT A SPECIFIC KEYWORD, CAN USE TO CREATE A STREAM OF TWEETS CREATED BY CERTAIN USER
#INPUT = NUMBER OF TWEETS AND USER, OUTPUT = ARRAY OF INDIVIDUAL TWEET STRINGS
#MAKE SURE TO OUTPUT AS TXT FILE

import tweepy
from tweepy.streaming import StreamListener
from tweepy import Stream
import json


ckey = 'anBC9SHrBRMkah3vL0djtUzuv'
csecret = 'OwfQRDpEo9HuwlLQFJZaaiJDvUbSLGPlhpV3kIqXaRBulAsFzk'
atoken = '1188729962-XuZUgmaVFFiTRnh7h3iE2e2XvISGdDQWH7uiPmO'
asecret = 'J0U97BpjzzwKHqUBBNPlpAuwWbkt4AgFkdpUJqlMQcsDw'

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

user = api.me()

print('Name ' + user.name)


class StdOutListener(StreamListener):
    ''' Handles data received from the stream. '''

    def __init__(self, max_results): 
        super(StdOutListener, self).__init__()
        self.text_output = open('tweet_text', 'w')
        self.date_output = open('tweet_dates', 'w')

        self.count = 0
        self.max_count = max_results

        if max_results:
            self.max_count = max_results
        else: 
            self.max_count = float("inf")

    def on_data(self, data):

        ## if we have not hit the limit, write all applicable data
        if self.count < self.max_count: 

            jd = json.loads(data)
            if self.count < self.max_count:

                if jd.has_key('text'):
                    self.text_output.write(jd['text'].encode('utf-8'))
                if jd.has_key('lang'):
                    self.text_output.write(jd['lang'])
                if jd.has_key('created_at'):
                    self.date_output.write(jd['created_at'].encode('utf-8'))

                if jd.has_key('text') or jd.has_key('lang'):
                    self.text_output.write("\n")
                    self.date_output.write("\n")

            ## increment
            self.count += 1
            return True
        else:
            self.text_output.close()
            self.date_output.close()
            print 'tweets = '+str(self.count)
            return False


    # 	return True

    def on_error(self, status):
    	print status


def extractPosts(keyword):
    twitterStream = Stream(auth, StdOutListener(3))
    twitterStream.filter(track=[keyword]) 

	#need to extract only posts and output to .txt file
 
extractPosts("car")





