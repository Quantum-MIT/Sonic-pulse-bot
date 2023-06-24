import openai 
import streamlit as st

# pip install streamlit-chat  
from streamlit_chat import message
openai.api_key = "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"

def generate_response(prompt):
    completions = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message 


#Creating the chatbot interface
st.title("chatBot : Streamlit + openAI")

# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

# We will get the user's input by calling the get_text function
def get_text():
    input_text = st.text_input("You: ","Hello, how are you?", key="input")
    return input_text
changes = '''
<style>
[data-testid="stAppViewContainer"]
{
background-image:url(https://images.unsplash.com/photo-1600044301600-492f228b5880?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80);
background-size:cover;
}
</style>
'''
user_input = get_text()

if user_input:
    output = generate_response(user_input)
    # store the output 
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
