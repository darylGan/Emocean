import hydralit_components as hc
import datetime

import streamlit as st
from PIL import Image
img = Image.open("images/logo.png")
st.set_page_config(
    page_title="Emocean",
    page_icon= img,
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

import streamlit.components.v1 as components
from track_utils import create_emotionclf_table
import utils.display as udisp

from src import home, dataVisualization, monitor, documentation, about

MENU = {
    "Home" : home,
    "Exploratory Data Analysis" : dataVisualization,
    "Monitor" : monitor,
    "Documentation" : documentation,
    "About" : about,
}

def main():
    menu_data = [
        {'icon': "far fa-chart-bar", 'label':"Exploratory Data Analysis"},  #no tooltip message
        {'icon': "fas fa-desktop",'label':"Monitor"},
        {'icon': "far fa-copy", 'label':"Documentation"},
        {'icon': "fas fa-info-circle", 'label':"About"}, 
    ]

    over_theme = {'txc_inactive': '#FFFFFF','menu_background':'#A7C7E7'}
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
