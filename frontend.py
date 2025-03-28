import streamlit as st 
st.set_page_config(layout="wide", page_title="LangGraph AI Agent")
st.title("LangGraph AI Agent")
st.markdown("This is a simple interface to interact with the LangGraph AI Agent. The AI Agent is a language model that can generate text based on a prompt. You can use this interface to chat with the AI Agent and see the responses it generates.")

system_prompt= st.text_area('Define you AI Agent:', placeholder='Type your prompt here...')

MODEL_NAMES_GROQ = ['llama3-70b-8192', 'mixtral-8x7b-32768', 'llama-3.3-70b-versatile']

MODEL_NAMES_OPENAI = ['gpt-4o-mini']

provider= st.selectbox('Select the model provider:', ['Groq', 'OpenAI'])

model_name= st.selectbox('Select the model name:', MODEL_NAMES_GROQ if provider=='Groq' else MODEL_NAMES_OPENAI)

allow_search= st.checkbox('Allow search')
user_query= st.text_area('Enter query:', placeholder='Type your query here...', height=150)
API_URL ='http://127.0.0.1:8000/chat'
if st.button('Chat'):
    if user_query.strip():
        import requests 
        response = requests.post(API_URL, json={
            'model_name': model_name,
            'model_provider': provider,
            'system_prompt': system_prompt,
            'messages': [user_query],
            'allow_search': allow_search
        })
        if response.status_code == 200:
            response_data = response.json()
            if 'error' in response_data:
                st.error(response_data['error'])
            st.markdown(f'AI Agent Response:{response_data}')
