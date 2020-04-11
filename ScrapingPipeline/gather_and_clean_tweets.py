import pandas as pd  
import numpy as np
from nltk.tokenize import WordPunctTokenizer
from bs4 import BeautifulSoup
import re

#Store these three files on S3 bucket(maybe) don't think its needed though
df_users = pd.read_excel("tweetsusers.xlsx")
df_random = pd.read_csv("tweetsrandom.csv")
df_kaggle = pd.read_csv("tweetskaggle.csv")

df_users = df_users.drop(['Created_at'],axis=1)
df_random = df_random.rename(columns={"Tweets": "Tweet"})
df_kaggle = df_kaggle.rename(columns={"Tweets": "Tweet"})
df_kaggle = df_kaggle.drop(['Created_At'],axis = 1)

frames = [df_users, df_kaggle, df_random]
df_tweets = pd.concat(frames,ignore_index= True)
#Write df_tweets as csv to S3 bucket for pipeline 


tok = WordPunctTokenizer()
pat1 = r'@[A-Za-z0-9]+'
pat2 = r'https?://[A-Za-z0-9./]+'
combined_pat = r'|'.join((pat1, pat2))
def tweet_cleaner(text):
    soup = BeautifulSoup(text, 'lxml')
    souped = soup.get_text()
    stripped = re.sub(combined_pat, '', souped)
    try:
        clean = stripped.decode("utf-8-sig").replace(u"\ufffd", "?")
    except:
        clean = stripped
    letters_only = re.sub("[^a-zA-Z]", " ", clean)
    lower_case = letters_only.lower()
    words = tok.tokenize(lower_case)
    return (" ".join(words)).strip()
	
clean_tweet_texts = []
for i in range(len(df_tweets.index)):
  clean_tweet_texts.append(tweet_cleaner(df_tweets['Tweet'][i]))
  

clean_tweets = pd.DataFrame(clean_tweet_texts,columns=['Tweet'])
# write clean_tweets to S3 bucket


