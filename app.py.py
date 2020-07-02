# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 22:04:19 2020

@author: MrROBOT
"""

import tweepy
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from textblob.np_extractors import ConllExtractor
import streamlit as st 


consumer_key= 'HrzPwaMKMHYoYmheWYONkT9lj'
consumer_secret= 'QFkYY54uDjYY1X5HMjYHDQbVXcbihNu8qydG9eR1AVJn7NQmcI'
access_token='860834802689298432-jwoqdMmw2ydXbm53AWMxRCM71jpajeK'
access_token_secret='vKhASPKJPp3J42HvPA5vHpFpYGY6iBLHyZTpk3HYd4T1c'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
def main():
    
    st.title("Twitter sentiment analysis‎")
    st.subheader("Discover the positive and negative opinions about a product")
    st.markdown("""
    	#### Sentiment analysis is the automated process of analyzing text data and sorting it into sentiments positive, negative, or neutral.
    	""")
    st.subheader("Search  by topic")
    message = st.text_area("Enter Text","Type Here ..")
    if st.button("Analyze"):
        new_tweets = api.search(q=message)
        for tweet in new_tweets:
            analysis = TextBlob(tweet.text, analyzer=NaiveBayesAnalyzer(), np_extractor= ConllExtractor())
            polarity = 'Positive'
            if (analysis.sentiment.p_pos < 0.50):
                polarity = 'Negative'
            st.subheader ("Sentiment Analysis and Topic of Interest")
            st.write(tweet.text)
            st.write(polarity)
            st.write("Confidence :  Positive score: " ,analysis.sentiment.p_pos*100, "  Negative score: ", analysis.sentiment.p_neg*100 )
            st.write ("Areas of interest: ", analysis.noun_phrases)
            st.subheader("---------------------------------------------------------------------------")      
            
    st.subheader('Enter a Twitter Username to search tweets for: ')
    messageID = st.text_area("Enter a ID here","...")
    if st.button("Process"):
        new_tweetsID = api.user_timeline(screen_name =messageID,count=20)
        for tweet in new_tweetsID:
            analysis = TextBlob(tweet.text, analyzer=NaiveBayesAnalyzer(), np_extractor= ConllExtractor())
            polarity = 'Positive'
            if (analysis.sentiment.p_pos < 0.50):
                polarity = 'Negative'
            st.subheader ("Sentiment Analysis and Topic of Interest")
            st.write ("Tweet : ",tweet.text)
            st.write ("Sentiment:",polarity)
            st.write("Confidence :  Positive score: " ,analysis.sentiment.p_pos*100, "  Negative score: ", analysis.sentiment.p_neg*100 )
            st.write ("Areas of interest: ", analysis.noun_phrases)
            st.subheader ("---------------------------------------------------------------------------")
    st.sidebar.subheader("About App")
    st.sidebar.text("TSA with Streamlit")
    st.sidebar.info("Cudos to the Streamlit Team")
    st.sidebar.subheader("Developed By")
    st.sidebar.text("Sahrul ALom Choudhari")
	            
if __name__ == '__main__':
	main()        
