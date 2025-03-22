import streamlit as st 

st.set_page_config(layout="wide", page_title="LangGraph AI Agent")
st.title("LangGraph AI Agent")
st.markdown("This is a simple interface to interact with the LangGraph AI Agent. The AI Agent is a language model that can generate text based on a prompt. You can use this interface to chat with the AI Agent and see the responses it generates.")

system_prompt= st.text_area('Define you AI Agent:', placeholder='Type your prompt here...')

MODEL