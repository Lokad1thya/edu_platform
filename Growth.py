import streamlit as st
from dotenv import load_dotenv
import os
from home import homepage
from about import about
from contact import contact
from rigel import rigel_page

# Sidebar navigation
page = st.sidebar.selectbox("Navigation", ["Home","Rigel","About","Contact"])

# Display the selected page
if page == "Home":
    homepage()
elif page == "About":
    about()
elif page == "Contact":
    contact()
elif page == "Rigel":
    rigel_page()
