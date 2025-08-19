import streamlit as st
import os
import re
from openai import OpenAI
from dotenv import load_dotenv
from RAG_function import get_pdf_paths


load_dotenv()
key_ct = os.environ["OPENAI_API_KEY"]
client = OpenAI(api_key=key_ct)

pdf_paths = get_pdf_paths("data/raw-pdfs")

pdf_names = {}
for path in pdf_paths:
    match = re.search(r"Acta.*(?=\.pdf$)", path)
    pdf_name = match.group(0) if match else ""
    pdf_names[pdf_name] = path


# Streamlit app

page_bg = """
<style>
.stApp {
background-color : #31cc74;
}
div.stButton > button:first-child {
    background-color: #cc9831;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)
st.title("Bot for TownHall Meetings info")

st.subheader("Dev Environment", divider="rainbow")


st.subheader("Choose the doc\n")

chosen_pdf = st.selectbox(
    "Choose the Record Meeting to interact with",
    (pdf_names),
    width=500,
)

st.subheader(f"What do you want to know about {chosen_pdf} ?\n")
current_question = st.text_area(
    "Ask your question",
    width="stretch",
)


st.markdown(["this is the test for ci"])
send_q = st.button("Send", type="primary", use_container_width=True, width="content")

st.write("now in branch dev")
if send_q:
    answer = st.write(
        f"You have asked  '{current_question}' about {chosen_pdf} that it's in {pdf_names[chosen_pdf]}"
    )
