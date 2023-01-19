import streamlit as st
from streamlit_lottie import st_lottie
import json

def space(num_lines=1):
    for _ in range(num_lines):
        st.write("")

def app():
    def title(text,size):
        st.markdown(f'<h3 style="font-weight:bolder;font-size:{size}px;text-align:center;">{text}</h3>',unsafe_allow_html=True)
    
    st.title("About the Dashboard")
    home_col_1, home_col_2, home_col_3= st.columns([10,2,1])

    with home_col_1:
        st.markdown("""

        <h2 style="font-weight:bolder;font-size:20px;color:#216fdb;text-align:left;">Malaysia’s Floods of December 2021: Can Future Disasters be Avoided?</h2> 
        
        """, unsafe_allow_html=True)
        st.markdown("""The floods of December 2021 in Malaysia left almost 50 dead, required the evacuation of about 400,000 people, and resulted in an overall estimate of RM6.1 billion in financial losses. Unprecedented volumes of rainfall left areas on the west coast of Peninsular Malaysia under almost four meters of water and turned roads into rivers.
        """)
 
    with home_col_3:
        st.write("")

    st.markdown("A video about the floods in 2021/2022:")

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
    <br/>
    <h2 style="font-weight:bolder;font-size:20px;color:#216fdb;text-align:left;">Sentiment & Emotion Flood Detection through Twitter</h2>
    
    This project was aimed to build a sentiment & emotion text analyzer about floods. 
    The dashboard can analyze how Malaysians react to the annual floods and what are their emotions. 
    
    <br/>
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

    The target users include:
    + General Public who are concerned about floods
    + Emergency Response Non-Profit Organizations (Mercy Malaysia; CREST Malaysia; Malaysian Red Crescent Society) 
    + Governmental Bodies (NADMA; Ministry Of Natural Resources, Environment And Climate Change)
    
    <br/>
    <h2 style="font-weight:bolder;font-size:20px;color:#216fdb;text-align:left;">Dataset</h2>

    The datasets used in this project is scraped from Twitter using Twitter API.     
    To access the dataset:   
    [English Dataset](https://drive.google.com/file/d/1U4ZgsQIhThBzvf26UK7er6mcWc4Z_aY-/view?usp=sharing)
    <br/>
    [Malay Dataset](https://drive.google.com/file/d/1Pvbf16V5SwidUbCDtxtLme0RyLCdEQK9/view?usp=sharing)

    <br/>
    <h2 style="font-weight:bolder;font-size:20px;color:#216fdb;text-align:left;">Source Code</h2>
    
    To access the source code:
    [Source Code](https://github.com/darylGan/Emocean)
    
    <br/>
    <h2 style="font-weight:bolder;font-size:20px;color:#216fdb;text-align:left;">About the Developer</h2>
    
    3rd year Bachelor of Computer Science (Data Science) student at University of Malaya
    <br/>
    Made in [Streamlit](https://www.streamlit.io/), by Daryl Gan | [GitHub](https://github.com/darylGan) | [LinkedIn](https://www.linkedin.com/in/daryl-gan-/)

    """, unsafe_allow_html=True)
