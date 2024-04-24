import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Import functions for data preprocessing & data preparation
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer, LancasterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import string
from string import punctuation
import nltk
import re
from textblob import TextBlob
import pandas as pd
import streamlit as st
import cleantext
st.header('Sentiment Analysis')
with st.expander('Analyze Text'):
    text = st.text_input('Text here: ')
    if text:
        blob = TextBlob(text)
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
def analyze_polarity_subjectivity(text):
    # Get polarity and subjectivity
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    return polarity, subjectivity
 
pre = st.text_input('Clean Text: ')
if pre:
        st.write(cleantext.clean(pre, clean_all= False, extra_spaces=True ,
                                 stopwords=True ,lowercase=True ,numbers=True , punct=True))

with st.expander('Analyze CSV'):
    upl = st.file_uploader('Upload file')

    def score(x):
        blob1 = TextBlob(x)
        return blob1.sentiment.polarity

#
    def analyze(x):
        if x < 0:
            return 'Negative'
        elif x ==0:
            return 'Neutral'
        else:
            return 'Posistive'


if upl:
        df = pd.read_excel(upl)
        df['score'] = df['Comment'].apply(score)
        df['analysis'] = df['score'].apply(analyze)
        st.write(df.head(10))

        @st.cache_data 
        def convert_df(df):
            # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(df)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='sentiments.csv',
            mime='text/csv',
        )
        
       
