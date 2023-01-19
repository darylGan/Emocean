import streamlit as st
import pandas as pd
import numpy as np
from wordcloud import WordCloud
import plotly.express as px 
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import text 

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

    # loading the data
    df = load_data()
    corpus = load_corpus()
    
    st.title("Explore Flood Emotions")
    space(1)
    st.markdown("""
    * Dataset Size: 3000 tweets
    * Time Period: 19th December 2021 - 31st January 2022
    """)
    space(1)
    st.write("***")

    space(1)
    st.subheader("Dataset")    
    with st.expander("Expand to Filter Dataset"):
        emotion_list = ['all', 'anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust']
        select_emotion = st.selectbox('select emotion',emotion_list)
        
        if select_emotion == 'all':
            df_selected_tweet = df
        else:
            df_selected_tweet = df[df[select_emotion]==1]

        st.header('Display Tweets of Selected Emotion(s)')
        st.write('Data Dimension: '+ str(df_selected_tweet.shape[0]) + ' rows and ' + str(df_selected_tweet.shape[1]) + ' columns.')
        st.dataframe(df_selected_tweet)    
    
    space(1)
    st.write("***")
    space(1)

    st.markdown('<h3 style="font-weight:lighter;font-size:50px;font-family:Source Sans Pro, sans-serif;text-align:center;">Visualization</h3>',unsafe_allow_html=True)
    space(2) 

    with st.container():
        col_1, col_2, col_3, col_4 = st.columns([2,0.5,7,1])
        with col_1:
            space(3)
            choiceSelection = st.radio("Choose a visualization", ("Emotion Distribution","Emotion Word Cloud","Common Words")) 

        with col_3:
            space(2)
            if choiceSelection=="Emotion Distribution":
                title('Distribution of Emotions',30)
                # ---------------------- Emotion Bar Chart ---------------------
                emotion_count = df['emotion'].value_counts().rename_axis('Emotions').reset_index(name='Counts')
                bar_CC = px.bar(emotion_count, x='Emotions', y='Counts', color='Emotions', color_discrete_sequence=px.colors.sequential.Plotly3)
                # bar_CC.update_xaxes(tickangle=0)
                bar_CC.update_layout(height=450) #margin_t=10,margin_b=150,
                st.plotly_chart(bar_CC,use_container_width=True)


            elif choiceSelection=="Emotion Word Cloud":
                #--------------------------WORD_CLOUD---------------------------
                title('Emotions WordCloud',30)

                unique_emotion = ['analytical','neutral','sadness','joy','anger','tentative','fear','confidence']
                sl = st.slider('Pick Number of Words',50,200)
                
                def grey_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
                    return("hsl(240,100%%, %d%%)" % np.random.randint(45,55))
                
                wc = WordCloud(stopwords=stop_words, background_color="white", color_func = grey_color_func, max_font_size=150, random_state=42,max_words=sl, collocations=False)

                plt.rcParams['figure.figsize'] = [30, 30]  #16,6 #40,40
                full_names = unique_emotion

                # Create subplots for each emotion
                for index, emotion in enumerate(corpus.emotion):
                    wc.generate(corpus.clean_tweet[emotion])
                    
                    plt.subplot(4, 2, index+1)  #3,4 #4,2
                    plt.imshow(wc, interpolation="bilinear")
                    plt.axis("off")
                    plt.title(full_names[index], fontsize = 40)
                    
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
