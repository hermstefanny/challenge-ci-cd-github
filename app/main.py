# Streamlit app
import streamlit as st

st.title("Bot for TownHall Meetings info")


st.subheader("Choose the doc\n")

subtype = st.selectbox(
    "Name of docs",
    ("ACTA 001", "ACTA 002"),
    width=200,
)

st.subheader("What do you want to know?\n")
current_question = st.text_area(
    "Ask your question",
    width="stretch",
)


send_q = st.button("Send", type="primary", use_container_width=True, width="content")

answer = st.write(current_question)
