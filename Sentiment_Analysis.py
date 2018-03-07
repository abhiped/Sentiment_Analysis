
# coding: utf-8

# In[13]:

from textblob import TextBlob
import tweepy
consumer_key=''#enter Consumer_key
consumer_secret=''#enter Consumer_secret
access_token=''#enter access_token
access_token_secret=''#enter access_token_secret
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
public_tweet=api.search('')#enter the tag you want to search!
t=0
c=0
for tweet in public_tweet:
    ##print(tweet.text)
    analysis=TextBlob(tweet.text)
    t=t+analysis.sentiment.polarity
    c=c+1
print(t/c)


# In[ ]:




# In[ ]:



