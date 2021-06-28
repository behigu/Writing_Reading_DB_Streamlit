import secondpage
import day5

import streamlit as st

PAGES = {
    "Home Page": day5,
    "Second Page": secondpage
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()