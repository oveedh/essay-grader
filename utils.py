import streamlit as st

def show_navigation():
    with st.container(border=True):
        col1,col2,col3,col4,col5=st.columns(5)
        col1.page_link("Hello.py", label="Log In", icon="🏠")
        col2.page_link("pages/upload_rubric.py", label="Rubrics", icon="1️⃣")
        col3.page_link("pages/upload_paper.py", label="Papers", icon="2️⃣")
        col4.page_link("pages/show_reviews.py", label="Reviews", icon="🌎")
        col5.page_link("pages/settings.py", label="Settings", icon="🌎")
        #cols=st.columns(len(navList)
        # col3.page_link("pages/1_chat_with_AI.py", label="Chat", icon="2️⃣", disabled=True)


