import streamlit as st
from streamlit_chat import message
from bardapi import Bard
import os
import requests
os.environ['_BARD_API_KEY'] = 'XwgHEyP9grTTPXFg1jwSs_RxcUW4_nJpVvlyRnSAshFg5y7Ei_JY7IvI6W94Zoo7tCbrdw.'
# token='xxxxxxx'

session = requests.Session()
session.headers = {
            "Host": "bard.google.com",
            "X-Same-Domain": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://bard.google.com",
            "Referer": "https://bard.google.com/",
        }
session.cookies.set("__Secure-1PSID", os.getenv("_BARD_API_KEY")) 
# session.cookies.set("__Secure-1PSID", token) 


#functions to generate output XwgHEyP9grTTPXFg1jwSs_RxcUW4_nJpVvlyRnSAshFg5y7Ei_JY7IvI6W94Zoo7tCbrdw.
def generate_response(prompt):
    token = 'XwgHEyP9grTTPXFg1jwSs_RxcUW4_nJpVvlyRnSAshFg5y7Ei_JY7IvI6W94Zoo7tCbrdw.'
    bard = Bard(token=token, session=session, timeout=30)
    response = bard.get_answer(prompt)['content']
    return response


def get_text():
    input_text = st.text_input("Mitadru's Bot: ", "", key='input')
    return input_text

#title
st.title("SonicPulse Bot")
#data-testid="stAppViewContainer"
changes = '''
<style>
[data-testid="stAppViewContainer"]
{
background-image:url(https://images.unsplash.com/photo-1600044301600-492f228b5880?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80);
background-size:cover;
}
</style>
'''
st.markdown(changes,unsafe_allow_html=True)
print(st.session_state)
if 'generate' not in st.session_state:
    st.session_state['generate'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
#accepting user input
user_input = get_text()
if user_input:
    print(user_input)
    response = generate_response(user_input)
    print(response)
    st.session_state.past.append(user_input)
    st.session_state.generate.append(response)

if st.session_state['generate']:
    for i in range(len(st.session_state['generate'])-1,-1,-1):
        message(st.session_state['past'][i], key="user_" + str(i), is_user=True)
        message(st.session_state['generate'][i],key=str(i))
        # message(st.session_state['past'][i], key="user_"+str(i),is_user=True)
