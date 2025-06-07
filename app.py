import streamlit as st
from summarizer import get_summary

st.title("📝 Transformer-based Text Summarizer")

user_input = st.text_area("Enter text to summarize:")

if st.button("Summarize"):
    if user_input:
        result = get_summary(user_input)
        st.subheader("Summary:")
        st.write(result)
    else:
        st.warning("Please enter some text first!")
