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
        footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown(
         f"""
         <style>
         .stApp {{background-image: url("https://images.unsplash.com/photo-1585854467604-cf2080ccef31?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8Ymx1ZSUyMHdhdmV8ZW58MHx8MHx8&w=1000&q=80");
                  background-size: cover}}
         </style>
         """, unsafe_allow_html=True)

import streamlit.components.v1 as components
from track_utils import create_emotionclf_table
import utils.display as udisp

from src import home, rumah, visualization, monitor, userManual, about

MENU = {
    "Home" : home,
    "Malay" : rumah,
    "Explore" : visualization,
    "Monitor" : monitor,
    "User Manual" : userManual,
    "About" : about,
}

def main():
    menu_data = [
        {'icon': "bi bi-translate", 'label':"Malay"},
        {'icon': "bi bi-bar-chart-line-fill", 'label':"Explore"},
        {'icon': "bi bi-tv-fill",'label':"Monitor"},
        {'icon': "bi bi-file-earmark-text-fill", 'label':"User Manual"},
        {'icon': "bi bi-info-circle-fill", 'label':"About"}, 
    ]

    over_theme = {'txc_inactive':'#FFFFFF','menu_background':'#000080','txc_active':'#000000','option_active':'#00FFFF'}
    
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
