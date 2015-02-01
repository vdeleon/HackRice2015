#!/usr/bin/env python

import flask
from flask import Flask, jsonify, request
import tweepy
from tweepy.streaming import StreamListener
from tweepy import Stream
import json

# Create the application.
APP = flask.Flask(__name__)



ckey = '3nis884mLWtLoFppAX7EGwlwC'
csecret = 'tcDmsh1vnpzxp04vjVZTps1rr4U2g0Cnkd5CgTvWsICrBTz07F'
atoken = '3006060253-GOGZkRZOa8p9tU2bxYLYHknKoLCC75DE5lFx5iD'
asecret = 'UAtu8khsOkHCUfDp0y5ahb1AV6GvcHVxPhz23lI1KtBCX'

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

user = api.me()
# print('Name ' + user.name)


class StdOutListener(StreamListener):
    

    def __init__(self, max_results): 
        super(StdOutListener, self).__init__()
        self.text_output = open('tweet_text.txt', 'w')
        self.date_output = open('tweet_dates.txt', 'w')

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
                    self.text_output.write("\n\n")
                    self.date_output.write("\n\n")

            ## increment
            print count
            self.count += 1
            return True
        else:
            self.text_output.close()
            self.date_output.close()
            print 'tweets = '+str(self.count)
            return False

    #   return True
    def on_error(self, status):
        print status


def extractPosts(keyword):
	twitterStream = Stream(auth, StdOutListener(100))
	twitterStream.filter(track=[keyword])


@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    
    return flask.render_template('index.html')

# @APP.route('/_add_numbers')
# def add_numbers():
#     a = request.args.get('a', 0, type=int)
#     b = request.args.get('b', 0, type=int)
#     return jsonify(result=a + b)


@APP.route('/search',  methods=['POST'])
def search():
    print "searching"
    data = request.form['data']
    extractPosts(data)
    return "Done Searching"

if __name__ == '__main__':
    APP.debug=True
    APP.run()
