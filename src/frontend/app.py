import streamlit as st
from streamlit_chat import message
from config import (SUGGEST_QUESTION_ENDPOINT, QUESTION_ANSWER_ENDPOINT)
import requests
import asyncio
import aiohttp
import json

industries = [
    "Agriculture",
    "Automotive",
    "Banking",
    "Biotechnology",
    "Chemical",
    "Construction",
    "Education",
    "Energy",
    "Entertainment",
    "Finance",
    "Food",
    "Healthcare",
    "Hospitality",
    "Information Technology",
    "Manufacturing",
    "Media",
    "Mining",
    "Pharmaceutical",
    "Retail",
    "Telecommunications",
    "Transportation",
    "Utilities"
]


# Title
st.title('LawBot: Question and Answer')

## 
user_profile = {}
user_role = 'user'
assistant_role = 'assistant'


st.session_state.setdefault(
    'mainchat',
    [{'type': 'assistant', 'message': 'Hello, how can i help you?'}]
)

st.session_state.setdefault(
    'questions_resp',
    []
)

def submit_profile():
    response = requests.post(SUGGEST_QUESTION_ENDPOINT, data=json.dumps(user_profile))
    question_obj = json.loads(response.text)
    st.session_state.questions_resp.clear()
    for question in question_obj['question_list']:
         st.session_state.questions_resp.append(question)

def ask_question(user_input):
    qa_resp = requests.post(QUESTION_ANSWER_ENDPOINT, data=json.dumps({'profile': user_profile, 'question': user_input}))
    return json.loads(qa_resp.text)


def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.mainchat.append({'type': 'user', 'message': user_input})
    qa_res_obj = ask_question(user_input)
    st.session_state.mainchat.append({'type': 'assistant', 'message': qa_res_obj['response']})
    st.session_state.user_input = ''


def on_suggestion(suggestion):
    st.session_state.mainchat.append({'type': 'user', 'message': suggestion})
    qa_res_obj = ask_question(suggestion)
    st.session_state.mainchat.append({'type': 'assistant', 'message': qa_res_obj['response']})
    st.session_state.user_input = ''


def generateMessage(chatDict):
    if chatDict['type'] == 'user':
        return message(chatDict['message'], is_user=True)
    else:
        return message(chatDict['message'])
    
def clear_suggestions():
    st.session_state.questions_resp.clear()

async def main():
    # Sidebar
    with st.sidebar:
        st.header('Profile')
        user_profile['name'] = st.text_input('Name')
        user_profile['age'] = st.number_input('Age', min_value=1, max_value=99, step=1)
        user_profile['employment_status'] = st.selectbox('Select Option', ['Employee', 'Employer'])
        user_profile['occupation'] = st.text_input('Occupation')
        user_profile['industry'] = st.selectbox('Industry', industries)

        st.button('submit profile', on_click=submit_profile)

    # Main chat
    chat_placeholder = st.empty()
    with chat_placeholder.container():
        for i in range(len(st.session_state['mainchat'])):
            generateMessage(st.session_state['mainchat'][i])


    # container for suggestion response
    container = st.container(border=True)
    with container:
        if len(st.session_state['questions_resp']) > 0:
               st.button("Clear suggestions", type="primary", on_click=clear_suggestions)
        for i in range(len(st.session_state['questions_resp'])): 
            st.button(st.session_state['questions_resp'][i], on_click=on_suggestion, key=f"{i}_{'questions_resp'}", args=(st.session_state['questions_resp'][i],))


    # Chat window
    with st.container():
        st.text_input("User Input:", on_change=on_input_change, key="user_input")

asyncio.run(main())
