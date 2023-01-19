import streamlit as st
import pandas as pd
import plotly.express as px 
from track_utils import view_all_prediction_details

def app():
    def title(text,size):
        st.markdown(f'<h3 style="font-weight:bolder;font-size:{size}px;text-align:center;">{text}</h3>',unsafe_allow_html=True)
        
    st.title("Analyzer Log Records")

    st.markdown("""<h2 style="font-weight:bolder;font-size:30px;color:#216fdb;text-align:left;">Emotion Text Analyzer History</h2>""",unsafe_allow_html=True)

    df_emotions = pd.DataFrame(view_all_prediction_details(),columns=['Input Text','Emotion','Score','Time of Visit'])
    st.dataframe(df_emotions, width=800)
    
    prediction_count = df_emotions['Emotion'].value_counts().rename_axis('Emotion').reset_index(name='Count')

    bar_CC = px.bar(prediction_count, x='Emotion', y='Count', color='Prediction', color_discrete_sequence=px.colors.qualitative.T10)
    bar_CC.update_xaxes()
    bar_CC.update_layout()
    st.plotly_chart(bar_CC,use_container_width=True)
