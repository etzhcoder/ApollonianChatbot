import streamlit as st
import os
from main import generate_response
import time


st.set_page_config(page_title="Apollonian Chatbot", page_icon="🤖")
st.title("Apollonian Chatbot")
st.write("Welcome to the Apollonian Chatbot, Ask me anything.")


if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": "You are a friendly and helpful medical assistant"}
    ]

with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("You:", "", key="input")
    cols = st.columns([1, 1])
    with cols[0]:
        send_button = st.form_submit_button(label='Send')
    with cols[1]:
        clear_button = st.form_submit_button(label='Clear Chat')
    
    if send_button and user_input:
        st.session_state['messages'].append({"role": "user", "content": user_input})

        with st.spinner("Bot is typing..."):
            bot_response = generate_response(st.session_state['messages'])
            time.sleep(1)

        st.session_state['messages'].append({"role": "assistant", "content": bot_response})

    if clear_button:
        st.session_state['messages'] = [
            {"role": "system", "content": "You are a friendly and helpful medical assistant."}
        ]

chat_container = st.container()
with chat_container:
    st.markdown("---")
    for message in st.session_state['messages']:
        if message['role'] == 'user':
            st.markdown(f"**You:** {message['content']}")
        elif message['role'] == 'assistant':
            st.markdown(f"**Bot:** {message['content']}")
    st.markdown("---")