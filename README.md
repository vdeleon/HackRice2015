# HackRice2015

Project written for the Rice Hackathon 2015. A web application that analyzes sentiment of tweets of a particular search keyword, and graphs the sentiment on a 5 point scale versus time (dates). The web application utilizes the python Tweepy library to gather tweets, hosts a Python script using Flask, and calls the Python script using AJAX. The ML Sentiment Analysis algorithm is from Stanford CoreNLP library and is written in Java. We didn't have time to fully autonomize the process of calling a java function from our web app. We graph our results using Google Charts.
