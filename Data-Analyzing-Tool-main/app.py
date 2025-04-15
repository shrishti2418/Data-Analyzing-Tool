import streamlit as st
from dotenv import load_dotenv
from utils import query_agent

load_dotenv()


st.title("Analyze Your CSV File 🤖")
st.header("Please Upload Your CSV File Over Here...")

# Capture the CSV File
data = st.file_uploader("Upload CSV File", type="csv")
query = st.text_area("Enter your query")
button = st.button("Generate Response")



if button:
    answer = query_agent(data, query)
    st.write(answer)