import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from pivottablejs import pivot_ui
from pygwalker.api.streamlit import StreamlitRenderer

st.set_page_config(
    page_title="Streamlit Data Analyzer",
    layout="wide"
)

st.title("Data Analyzer")

st.sidebar.subheader("Setting")
uploaded_file = st.sidebar.file_uploader(label="Upload your CSV or Excel file.",type=['csv','xlsx'])

df = pd.DataFrame()
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        df = pd.read_excel(uploaded_file)


if not df.empty:
    try:
        #st.write(df)

        st.subheader("Pivot Table")
        t = pivot_ui(df)
        with open(t.src) as t:
            components.html(t.read(), None, height=1000, scrolling=True)

        st.subheader('Visualizer')
        p = StreamlitRenderer(df)
        p.explorer()

    except Exception as e:
        st.write('Exception: %s', repr(e))
else:
    st.write("Please upload a file...")