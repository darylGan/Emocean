import streamlit as st

def app():
    def title(text,size):
        st.markdown(f'<h3 style="font-weight:bolder;font-size:{size}px;text-align:center;">{text}</h3>',unsafe_allow_html=True)

    st.title("User Manual")

    st.markdown("""
    <h2 style="font-weight:bolder;font-size:30px;color:#216fdb;text-align:left;">User Manual Document</h2>

    <p>To find out more details about this application, please refer to this <a target="_blank" href="https://drive.google.com/file/d/1-yYgNFvHSfUtbJ-uMhLR-u9RcCLOKU65/view?usp=sharing">user manual.</a></p>

    <h2 style="font-weight:bolder;font-size:30px;color:#216fdb;text-align:left;">Home</h2>

    **Home** has a **Flood & Sentiment & Emotion Text Analyzer** which is developed by training 3 machine learning models.
    It can determine whether a text is flood related or not as well as the sentiment and emotion of user input text.
    Text or tweets can be typed in the textbox and the analysis results will be generated after the *Analyze* button is clicked.

    <h2 style="font-weight:bolder;font-size:30px;color:#216fdb;text-align:left;">Versi Melayu</h2>

    **Versi Melayu** mempunyai **Penganalisis Teks Banjir & Sentimen & Emosi** yang dibangunkan dengan melatih 3 model pembelajaran mesin.
    Ia boleh menentukan adakah teks berkaitan dengan banjir atau tidak serta sentimen dan emosi teks input pengguna.
    Teks atau tweets boleh ditaip dalam kotak teks dan keputusan analisis akan dihasilkan selepas butang *Analisis* ditekan.
    
    <h2 style="font-weight:bolder;font-size:30px;color:#216fdb;text-align:left;">Explore</h2>

    **Explore** the dataset by filtering it according to emotions of interest or by plotting various insightful visualizations such as Bar Charts & Word Clouds.
    The datasets that are used in this project and some of the sample tweets of each category of emotion can be viewed.
    The distribution of emotions in the dataset, typical words used in each emotion, and common words or combination of words can be explored.
   
    <h2 style="font-weight:bolder;font-size:30px;color:#216fdb;text-align:left;">Analyzer Log</h2>

    **Analyzer Log** records the user input text in **Flood & Sentiment & Emotion Text Analyzer** & **Penganalisis Teks Banjir & Sentimen & Emosi**.
    Analyzed text in the past and its analysis results can be found here.
    
    <h2 style="font-weight:bolder;font-size:30px;color:#216fdb;text-align:left;">About</h2>

    **About** introduces **Emocean**, which include details about this application, its background; ideation; objectives; stakeholders; and information about the developer.

    """,unsafe_allow_html=True)
