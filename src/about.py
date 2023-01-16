import streamlit as st
from streamlit_lottie import st_lottie
import json

def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")

def app():
    st.markdown(f'<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">', unsafe_allow_html=True)
    st.markdown("""
        <style>
        blockquote.twitter-tweet {
            display: inline-block;
            font-family: "Helvetica Neue", Roboto, "Segoe UI", Calibri, sans-serif;
            font-size: 12px;
            font-weight: bold;
            line-height: 16px;
            border-color: #eee #ddd #bbb;
            border-radius: 5px;
            border-style: solid;
            border-width: 1px;
            box-shadow: 0 1px 3px rgb(0 0 0 / 20%);
            margin: 10px 5px;
            padding: 8px 16px 16px 16px;
            max-width: 468px;
            transition: transform 500ms ease;
        }
        .twitter-tweet:hover,
        .twitter-tweet:focus-within {
            transform: scale(1.025);
        }
        </style>""",unsafe_allow_html=True)
        
    #st.subheader("About")
    
    st.title("About the Application")
    home_col_1, home_col_2, home_col_3= st.columns([10,2,1])

    with home_col_1:
        st.markdown("""

        <h2 style="font-weight:bolder;font-size:20px;color:#216fdb;text-align:left;">Malaysia’s Floods of December 2021: Can Future Disasters be Avoided?</h2> 
        
        """, unsafe_allow_html=True)
        st.markdown("""The floods of December 2021 in Malaysia left almost 50 dead, required the evacuation of about 400,000 people, and resulted in an overall estimate of RM6.1 billion in financial losses. Unprecedented volumes of rainfall left areas on the west coast of Peninsular Malaysia under almost four meters of water and turned roads into rivers.
        """)
 
    with home_col_3:
        st.write("")
    # Video
    st.markdown("A video about the floods in 2021/2022")

    abt_col_1, abt_col_2, abt_col_3, abt_col_4,abt_col_5 = st.columns([0.1,2,1,1.5,1])
    with abt_col_1:
        st.write("")
    with abt_col_2:
        st.video("https://www.youtube.com/watch?v=N6q5iVFxAlc")
    with abt_col_3:
        st.write("")
    with abt_col_4:
        st.write("")
    with abt_col_5:
        st.write("")
    
    st.markdown("""
    <h2 style="font-weight:bolder;font-size:20px;color:#216fdb;text-align:left;">Sentiment & Emotion Flood Detection through Twitter</h2>
    
    This project aims to build a sentiment & emotion analyzer about floods. 
    The application can analyze how Malaysians react to the floods and what are their emotions. 
    The application can also analyze the emotion from the user input text. 
    
    <h2 style="font-weight:bolder;font-size:20px;color:#216fdb;text-align:left;">Objectives</h2>

    1. To identify sentiment and emotion by using supervised machine learning algorithms.
        - What algorithms can identify sentiment and emotion from tweets?
        
        <br/>

    2.  To develop a sentiment and emotion-based flood detection model for English and Malay.
        - How to develop a machine learning model for different languages?
        
        <br/>
        
    3.  To evaluate the effectiveness of the flood detection model by using evaluation metrics.
        - What metrics can evaluate the effectiveness of the machine learning model?
        
        <br/>

    4.  To build a sentiment and emotion-based flood detection dashboard.
        - How can stakeholders be informed about the data insights and the use of the model?
        
        <br/>
        
    <h2 style="font-weight:bolder;font-size:20px;color:#216fdb;text-align:left;">Stakeholders</h2>

    <p>Anyone can use this App completely for free! The target users include the general public who are concerned about floods, emergency response non-profit organizations and governmental bodies such as the Ministry Of Natural Resources, Environment And Climate Change.
 
    <h2 style="font-weight:bolder;font-size:20px;color:#216fdb;text-align:left;">Features</h2>
    
    + Sentiment & Emotion Prediction
    + Data Exploration and Analysis
    + Monitoring Application

    <h2 style="font-weight:bolder;font-size:20px;color:#216fdb;text-align:left;">Dataset</h2>

    The dataset used in this project is scraped from Twitter using Twitter API.     
    To access the dataset:   
    https://drive.google.com/drive/folders/...

    <h2 style="font-weight:bolder;font-size:20px;color:#216fdb;text-align:left;">Source Code</h2>

    https://github.com/darylGan/Emocean
    
    <h2 style="font-weight:bolder;font-size:20px;color:#216fdb;text-align:left;">About the Developer</h2>
    3rd year Bachelor of Computer Science (Data Science) student at University of Malaya

    Made in [Streamlit](https://www.streamlit.io/) &nbsp, by Daryl Gan &nbsp | &nbsp [GitHub](https://github.com/darylGan) &nbsp | &nbsp [LinkedIn](https://www.linkedin.com/in/daryl-gan-/)

    """, unsafe_allow_html=True)
