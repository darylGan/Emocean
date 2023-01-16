import streamlit as st

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

    st.title("Documentation")

    st.markdown("""
    <h2 style="font-weight:bolder;font-size:30px;color:#216fdb;text-align:left;">The Menu</h2>

    <p>To read more details about this application, can refer to <a target="_blank">user manual.</a></p>

    <h2 style="font-weight:bolder;font-size:25px;color:#216fdb;text-align:left;">Home</h2>

    **Home** has a text emotion analyzer which is a trained machine learning model that is used to predict the emotion of the user input text. Text or tweets can be input into the textbox and click the *Analyze* button to generate the analysis result.

    <h2 style="font-weight:bolder;font-size:25px;color:#216fdb;text-align:left;">Explore</h2>

    **Explore** the dataset by plotting various insightful visualizations such as Bar Chart & Word Cloud. The datasets that are used in this project and some of the sample tweets of each category of sentiment & emotion can be inspected. The distribution of emotions in the dataset, which words are mostly used in each emotion, which word and combination of words are most popular can be explored.
    
    IMPORTANT: It might take some time for the results to load due to the large dataset that is needed to process. 

    <h2 style="font-weight:bolder;font-size:25px;color:#216fdb;text-align:left;">Monitor</h2>

    **Monitor** records the input text data in sentiment & emotion analyzer from the user. The past analyzed text entered by users in **Home** and the results can be found here.
    
    <h2 style="font-weight:bolder;font-size:25px;color:#216fdb;text-align:left;">About</h2>

    **About** introduces *Floods*, details about this application, and the information about the developer.

    """,unsafe_allow_html=True)
