import streamlit as st
import requests

st.title("Customer Service Chatbot")

user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        response = requests.post(
            "http://127.0.0.1:5000/chatbot",
            json={"query": user_input}
        ).json()
        st.text_area("Bot:", value=response['response'], height=200)
