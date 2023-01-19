import streamlit as st
import hydralit_components as hc
import datetime

from PIL import Image
img = Image.open("images/logo.png")
st.set_page_config(
    page_title="Emocean",
    page_icon=img,
    layout="wide",
    initial_sidebar_state="collapsed",
)

hide_streamlit_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://media.istockphoto.com/id/1389811180/vector/flood-in-town-natural-disaster-with-rain-storm.jpg?s=612x612&w=0&k=20&c=qEvkOWgbADBK3pioS3WbaF-KTj7-uqMp4nQtF6j7CDU=");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

import streamlit.components.v1 as components
from track_utils import create_emotionclf_table
import utils.display as udisp

from src import home, visualization, monitor, userManual, about

MENU = {
    "Home" : home,
    "Explore" : visualization,
    "Monitor" : monitor,
    "User Manual" : userManual,
    "About" : about,
}

def main():
    menu_data = [
        {'icon': "bi bi-bar-chart-line-fill", 'label':"Explore"},
        {'icon': "bi bi-tv-fill",'label':"Monitor"},
        {'icon': "bi bi-file-earmark-text-fill", 'label':"User Manual"},
        {'icon': "bi bi-info-circle-fill", 'label':"About"}, 
    ]

    over_theme = {'txc_inactive':'#000000','menu_background':'#A7C7E7','txc_active':'#FFFFFF','option_active':'#000080'}
    
    menu_id = hc.nav_bar(
        menu_definition=menu_data,
        override_theme=over_theme,
        home_name='Home',
        hide_streamlit_markers=False,
        sticky_nav=True,
        sticky_mode='pinned',
    )
    
    menu = MENU[menu_id]
    menu_selection = menu_id
    with st.spinner(f"Loading {menu_id} ..."):
        udisp.render_page(menu)

if __name__ == '__main__':
    main()
