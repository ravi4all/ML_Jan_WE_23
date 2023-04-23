import streamlit as st
import summarization

st.set_page_config(layout="wide")

st.title("Text Summarization Application")
st.write("This app lets you summarize a given text")

form = st.form("summary")
text = form.text_area("Enter/Paste your text here")
btn = form.form_submit_button("Generate Summary")

if btn:
    summary = summarization.generate(text)
    st.write(summary)