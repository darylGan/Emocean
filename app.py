# Core Pkgs
from PIL import Image
img = Image.open("images/logo.png")
import streamlit as st
st.set_page_config(
    page_title="Emocean",
    page_icon= img,
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'About': "### Sentiment & Emotion-based Flood Detection through Twitter"
    }
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
# import your app modules here
from src import home, dataVisualization, monitor, documentation, about


import hydralit_components as hc
import datetime


MENU = {
    "Home" : home,
    "Exploratory Data Analysis" : dataVisualization,
    "Monitor" : monitor,
    "Documentation" : documentation,
    "About" : about,
    
}

def main():
    
    # specify the primary menu definition
    menu_data = [
        {'icon': "far fa-chart-bar", 'label':"Exploratory Data Analysis"},#no tooltip message
        {'icon': "fas fa-desktop",'label':"Monitor"},
        {'icon': "far fa-copy", 'label':"Documentation"},
        {'icon': "fas fa-info-circle", 'label':"About"}, 
    ]

    #create_emotionclf_table()

    over_theme = {'txc_inactive': '#FFFFFF','menu_background':'#35558A'}
    menu_id = hc.nav_bar(
        menu_definition=menu_data,
        override_theme=over_theme,
        home_name='Home',
        hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
        sticky_nav=True, #at the top or not
        sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
    )

    
    # st.sidebar.title("Navigate yourself...")
    # menu_selection = st.sidebar.radio("Menu", list(MENU.keys()))

    menu = MENU[menu_id]
    menu_selection = menu_id
    with st.spinner(f"Loading {menu_id} ..."):
        udisp.render_page(menu)



if __name__ == '__main__':
    main()
