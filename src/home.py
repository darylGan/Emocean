import streamlit as st
from track_utils import add_prediction_details
from datetime import datetime
import pandas as pd
import numpy as np
import neattext as nt
from neattext.functions import clean_text
from imblearn.pipeline import Pipeline, make_pipeline
import joblib
from sklearn.feature_extraction import text 

def space(num_lines=1):
    for _ in range(num_lines):
        st.write("")

st.set_option('deprecation.showPyplotGlobalUse', False)

#Stop Words
add_stop_words = ['you know','i mean','yo','dude','couldnt','cant','dont','doesnt','youve','im','ive','wasnt','mightnt','hadnt','hvnt','youre','wouldnt','shouldnt','arent','isnt','werent','youll','its','thats','know','people','amp','time','need','like','year','term','risk','work','gonna','gon na','u','na','sri','dm','tl','bc','cause','ya','w','taman','muda','shah','alam','hulu','langat']
english_stop_words = text.ENGLISH_STOP_WORDS.union(add_stop_words)
custom_stop_word_list = ['flood', 'help', 'come', 'day', 'feel', 'let', 'love', 'stay', 'water', 'victim', 'make', 'think', 'god', 'want', 'guy', 'bad', 'pls', 'malaysia', 'today', 'tweet', 'open', 'life', 'really', 'say', 'safe', 'pray', 'rain']
english_stop_words = english_stop_words.union(custom_stop_word_list)
#Stop Words

def cleantext(docx):
    docxFrame = nt.TextFrame(text=docx)
    docxFrame.remove_hashtags()
    docxFrame.remove_userhandles()
    docxFrame.remove_multiple_spaces()
    docxFrame.remove_urls()
    docxFrame.remove_emails()
    docxFrame.remove_numbers()
    docxFrame.remove_emojis()
    docxFrame.remove_puncts()
    docxFrame.remove_special_characters()
    docxFrame.remove_non_ascii()
    docxFrame.remove_stopwords()
    
    cleanDocx = docxFrame.text
    cleanDocx = clean_text(cleanDocx, contractions=True, stopwords=True)
    cleanDocx = ' '.join(term for term in cleanDocx.split() if term not in english_stop_words)
    return cleanDocx

#English Flood Analyzer
eng_flood_model = joblib.load("models/english_flood_related_mnb.pkl","r")

def predictFlood(docx):
    results = eng_flood_model.predict([docx])
    return results[0]
#English Flood Analyzer

#English Sentiment Analyzer
eng_sentiment_model = joblib.load("models/english_sentiment_svm.pkl","r")

def predictSentiment(docx):
    results = eng_sentiment_model.predict([docx])
    return results[0]
#English Sentiment Analyzer

emotions_emoji_dict = {"anger":"😡","anticipation":"🤔","disgust":"🤢","fear":"😨","joy":"😂","sadness":"😔","surprise":"😲","trust":"🤗"}

#English Emotion Analyzer
dfEng = pd.read_pickle("datasets/DSPEnglishTweetsCleanedV2.pkl")

from sklearn.model_selection import train_test_split
dfEng_subset = dfEng[dfEng['neutral'] != 1]
train, test = train_test_split(dfEng_subset, shuffle=True, test_size=0.2, random_state=42)
X_emotion_train = train['Tweets']
y_emotion_train = train[['anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust']]
X_emotion_test = test['Tweets']
y_emotion_test = test[['anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust']]

eng_emotion_model = joblib.load("models/english_emotion_rf.pkl","r")

def get_prediction_proba(docx):
    emotion = ['anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust']
    results = pd.DataFrame(columns=['anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust'])
    for label in emotion:
        eng_emotion_model.fit(X_emotion_train, train[label])

        test_y_prob = eng_emotion_model.predict_proba([docx])[:,1]
        results[label] = test_y_prob
    return results
#English Emotion Analyzer

def app():
    col_1, col_2, col_3 = st.columns([1,8,1])

    with col_1:
        st.write()
    
    with col_2:
        st.image("images/name.png")
        st.markdown('<h1 style="font-weight:10;font-size: 50px;font-family:Source Sans Pro, sans-serif;text-align:center;">Sentiment & Emotion-based Flood Detection through Twitter</h1>',unsafe_allow_html=True)
        
        space(2)
        st.subheader("Flood & Sentiment & Emotion Text Analyzer")
        space(1)
        st.markdown("**Instructions:** Enter Text")

        with st.form(key='emotion_form'):
            raw_text = st.text_area('Type Here: -',"")
            cleanDocx = cleantext(raw_text)
            submit_english_text = st.form_submit_button(label='Analyze')

    if submit_english_text:
        col1, col2, col3, col4 = st.columns([1,2,4,1])

        testing = predictFlood(cleanDocx)
        testingSentiment = predictSentiment(cleanDocx)
        probability = get_prediction_proba(cleanDocx)
        prediction = pd.DataFrame(probability.idxmax(axis=1))

        with col2:
            st.success("Prediction")
            if testing == 0:
                st.write("Non-Flood Related")
            else:
                st.write("Flood Related")         
            
            st.write("Sentiment: {}".format(testingSentiment))
            
            value = prediction.loc[0][0]
            emoji_icon = emotions_emoji_dict[value]
            st.write("Emotion: {} {}".format(value,emoji_icon))
            st.write("Emotion Score: {:.0%}".format(np.max(probability.to_numpy())))
            
            add_prediction_details(raw_text,value,np.max(probability.to_numpy()),datetime.now())
            
        with col3:
            st.success("Emotion Score")
            proba_df = probability
            porba_df_clean = proba_df.T.reset_index()
            porba_df_clean.columns = ["emotions","probability"]

            import plotly.express as px 
            bar_CC = px.bar(porba_df_clean, x='emotions', y='probability', color='emotions',color_discrete_sequence=px.colors.qualitative.T10)

            bar_CC.update_xaxes()
            bar_CC.update_layout()
            st.plotly_chart(bar_CC,use_container_width=True)
            
    else:
        with col_2: 
            st.write("*Click 'Analyze' Button*")
