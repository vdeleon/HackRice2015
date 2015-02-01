#CREATES A STREAM TO LISTEN TO TWEETS ABOUT A SPECIFIC KEYWORD, CAN USE TO CREATE A STREAM OF TWEETS CREATED BY CERTAIN USER
#INPUT = NUMBER OF TWEETS AND USER, OUTPUT = ARRAY OF INDIVIDUAL TWEET STRINGS
#MAKE SURE TO OUTPUT AS TXT FILE


import tweepy
from tweepy.streaming import StreamListener
from tweepy import Stream


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
 
    # def on_status(self, status):
    #     # Prints the text of the tweet
    #     print('Tweet text: ' + status.text)
 
    #     # There are many options in the status object,
    #     # hashtags can be very easily accessed.
    #     for hashtag in status.entries['hashtags']:
    #         print(hashtag['text'])
 
    #     return true
 
    # def on_error(self, status_code):
    #     print('Got an error with status code: ' + str(status_code))
    #     return True # To continue listening
 
    # def on_timeout(self):
    #     print('Timeout...')
    #     return True # To continue listening

    def on_data(self, data):
    	print data
    	return True

    def on_error(self, status):
    	print status


def extractPosts(keyword):
	twitterStream = Stream(auth, StdOutListener())
	twitterStream.filter(track=[keyword])

	#need to extract only posts and output to .txt file
 
extractPosts("car")





