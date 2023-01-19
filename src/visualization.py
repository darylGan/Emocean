import streamlit as st
import pandas as pd
import numpy as np
from wordcloud import WordCloud
import plotly.express as px 
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import text 
import seaborn as sns

def space(num_lines=1):
    for _ in range(num_lines):
        st.write("")

@st.cache(allow_output_mutation=True)
def load_data():
    data = pd.read_pickle("datasets/DSPEnglishTweetsCleanedV2.pkl")
    return data

@st.cache(allow_output_mutation=True)
def load_corpus():
    data = pd.read_pickle("datasets/DSPEnglishTweetsCorpus.pkl")
    return data

@st.cache(allow_output_mutation=True)
def load_dtm():
    data = pd.read_pickle("datasets/DSPEnglishTweetsDTMv2.pkl")
    return data

@st.cache(persist=True,suppress_st_warning=True)
def get_top_text_ngrams(corpus, ngrams=(1,1), nr=None):
    vec = CountVectorizer(stop_words=stop_words, ngram_range=ngrams).fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0)
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
    return words_freq[:nr]

add_stop_words = ['you know','i mean','yo','dude','couldnt','cant','dont','doesnt','youve','im','ive','wasnt','mightnt','hadnt','hvnt','youre','wouldnt','shouldnt','arent','isnt','werent','youll','its','thats','know','people','amp','time','need','like','year','term','risk','work','gonna','gon na','u','na','sri','dm','tl','bc','cause','ya','w','taman','muda','shah','alam','hulu','langat']
stop_words = text.ENGLISH_STOP_WORDS.union(add_stop_words)
custom_stop_word_list = ['flood', 'help', 'come', 'day', 'feel', 'let', 'love', 'stay', 'water', 'victim', 'make', 'think', 'god', 'want', 'guy', 'bad', 'pls', 'malaysia', 'today', 'tweet', 'open', 'life', 'really', 'say', 'safe', 'pray', 'rain']
stop_words = stop_words.union(custom_stop_word_list)

st.set_option('deprecation.showPyplotGlobalUse', False)

def app():
    def title(text,size):
        st.markdown(f'<h3 style="font-weight:bolder;font-size:{size}px;text-align:center;">{text}</h3>',unsafe_allow_html=True)

    def header(text):
        st.markdown(f"<p style='color:white;'>{text}</p>",unsafe_allow_html=True)

    df = load_data()
    corpus = load_corpus()
    dtm = load_dtm()
    
    st.title("Explore Emotions of Flood")
    space(1)
    st.markdown("""
    * Dataset Size: 3000 Tweets
    * Time Period: 19th December 2021 - 31st January 2022
    """)
    space(1)
    st.write("***")

    space(1)
    st.subheader("Dataset")    
    with st.expander("Expand to View Dataset"):
        emotion_list = ['all', 'anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust']
        space(1)
        select_emotion = st.selectbox('Select Emotion to Display Related Tweets:',emotion_list)
        
        if select_emotion == 'all':
            df_selected_tweet = df
        else:
            df_selected_tweet = df[df[select_emotion]==1]

        st.write('Data Dimension: '+ str(df_selected_tweet.shape[0]) + ' tweets and ' + str(df_selected_tweet.shape[1]) + ' attributes.')
        st.dataframe(df_selected_tweet)    
    
    space(1)
    st.write("***")
    space(1)

    st.markdown('<h3 style="font-size:50px;font-family:Source Sans Pro, sans-serif;text-align:center;">Visualizations</h3>',unsafe_allow_html=True)
    space(2) 

    with st.container():
        col_1, col_2, col_3, col_4 = st.columns([2,0.5,7,1])
        with col_1:
            choiceSelection = st.radio("Choose a Visualization", ("Emotion Distribution","Emotion Word Cloud","Common Words")) 

        with col_3:
            space(2)
            if choiceSelection=="Emotion Distribution":
                title('Distribution of the Number of Emotions per English Tweet',30)

                fig = plt.figure(figsize=(20,10))
                sns.set(font_scale=10)
                sns.countplot(df.emotion_count, palette='gist_rainbow')
                plt.xlabel("Number of Emotions")
                plt.ylabel("Number of Tweets")
                st.pyplot(fig)

            elif choiceSelection=="Emotion Word Cloud":
                title('Emotion Word Cloud',30)

                sl = st.slider('Choose Number of Words',50,200)
 
                def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
                    return("hsl(240,100%%, %d%%)" % np.random.randint(45,55))

                wc = WordCloud(stopwords=stop_words, background_color="white", color_func = grey_color_func, max_font_size=150, random_state=42, max_words=sl, collocations=False)

                plt.rcParams['figure.figsize'] = [20, 20]

                full_names = emotion = ['anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust']

                for index, emotion in enumerate(dtm.columns):
                    wc.generate(corpus.Tweets[emotion])

                    plt.subplot(4, 2, index+1)
                    plt.imshow(wc, interpolation="bilinear")
                    plt.axis("off")
                    plt.title(full_names[index], fontsize = 20)

                st.pyplot()

            elif choiceSelection=="Common Words":
                #-------------------------Module 1-----------------------------
                title('Most Popular One Word',30)
                # st.caption('removing all the stop words in the sense common words.')

                sl_2 = st.slider('Pick Number of Words',5,50,10, key="1")

                # Unigrams - Most Popular One Keyword
                top_text_bigrams = get_top_text_ngrams(corpus.clean_tweet, ngrams=(1,1), nr=sl_2)
                top_text_bigrams = sorted(top_text_bigrams, key=lambda x:x[1], reverse=False)
                x, y = zip(*top_text_bigrams)
                bar_C1 = px.bar(x=y,y=x, color=y, labels={'x':'Number of words','y':'Words','color':'frequency'}, title='Most Popular One Word', text=y, color_continuous_scale=px.colors.sequential.Plotly3[::-1])
                bar_C1.update_traces(textposition="outside", cliponaxis=False)
                bar_C1.update_yaxes(dtick=1, automargin=True)

                st.plotly_chart(bar_C1,use_container_width=True)

                #-------------------------Module 2-----------------------------
                title('Most Popular Two Words',30)

                sl_3 = st.slider('Pick Number of Words',5,50,10, key="2")

                # Unigrams - Most Popular One Keyword
                top_text_bigrams = get_top_text_ngrams(corpus.clean_tweet, ngrams=(2,2), nr=sl_3)
                top_text_bigrams = sorted(top_text_bigrams, key=lambda x:x[1], reverse=False)
                x, y = zip(*top_text_bigrams)
                bar_C2 = px.bar(x=y,y=x, color=y, labels={'x':'Number of words','y':'Words','color':'frequency'}, title='Most Popular Two Word', text=y, color_continuous_scale='Plotly3_r')
                bar_C2.update_traces(textposition="outside", cliponaxis=False)
                bar_C2.update_yaxes(dtick=1, automargin=True)

                st.plotly_chart(bar_C2,use_container_width=True)

                #-------------------------Module 3-----------------------------
                title('Most Popular Three Words',30)

                # header("range")
                sl_4 = st.slider('Pick Number of Words',5,50,10, key="3")

                # Unigrams - Most Popular One Keyword
                top_text_bigrams = get_top_text_ngrams(corpus.clean_tweet, ngrams=(3,3), nr=sl_4)
                top_text_bigrams = sorted(top_text_bigrams, key=lambda x:x[1], reverse=False)
                x, y = zip(*top_text_bigrams)
                bar_C3 = px.bar(x=y,y=x, color=y, labels={'x':'Number of words','y':'Words','color':'frequency'}, title='Most Popular Three Word', text=y,color_continuous_scale='Plotly3_r')
                bar_C3.update_traces(textposition="outside", cliponaxis=False)
                bar_C3.update_yaxes(dtick=1, automargin=True)

                st.plotly_chart(bar_C3,use_container_width=True) 
        
        with col_4:
            st.write("")
            space(2)
