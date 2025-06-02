import asyncio 
import random 
from langchain_ollama import OllamaLLM
import nest_asyncio 
from dotenv import load_dotenv 
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage 
import streamlit as st 
from agent import ask, create_history 
from client import connect_to_server 
from config import Config 
from models import create_llm 
from tools import load_tools 
import traceback
load_dotenv() 


LOADING_MESSAGES = [ 
"Organizing your tasks...", 
"Prioritizing your day...", 
"Consulting my digital checklist...", 
"Processing your request...", 
"Boosting your productivity...", 
"Analyzing your to-do list...", 
"Scheduling your success...", 
"Making sense of the task chaos...", 
"Getting your ducks (or tasks) in a row...", 
"Calculating the optimal plan...", 
"Tackling your task list...", 
"Brewing a potion of productivity...", 
"Streamlining your workflow...", 
"Checking things off the list...", 
"Thinking about vour next steps...",
]

async def get_response_async(user_query:str,history:list,llm):
    async with connect_to_server() as session:
        tools = await load_tools(session)
        llm_with_tools = llm.bind_tools(tools)
        response = await ask(
            user_query,
            history.copy(),
            llm_with_tools,
            tools,
        )
        return response
    
nest_asyncio.apply()

st.set_page_config(
    page_title="Task Manager",
    page_icon=":robot:",
    layout="centered",
)

st.title("Task Manager")
st.subheader("Your personal productivity assistant")


if "llm" not in st.session_state:
    st.session_state.llm = create_llm(Config.MODEL)

if "messages" not in st.session_state:
    st.session_state.messages = create_history()


for message in st.session_state.messages:
    if type(message) == SystemMessage:
        continue
    is_user = type(message) is HumanMessage
    avatar = "🤖" if is_user else "🧑"
    with st.chat_message("user" if is_user else "ai", avatar=avatar):
        st.markdown(message.content)
       

if prompt := st.chat_input("What can I help you with?"): 
    st.session_state.messages.append(HumanMessage(prompt)) 
    with st.chat_message("human", avatar="🧑") : 
        st.markdown(prompt) 
    with st.chat_message("assistant", avatar="🤖"): 
        message_placeholder = st.empty() 
        message_placeholder.status(random.choice (LOADING_MESSAGES), state="running") 

        try:
           response = asyncio.run(get_response_async(prompt, st.session_state.messages, st.session_state.llm))
        except* Exception as eg:
            for e in eg.exceptions:
                print(f"Sub-exception: {type(e).__name__} - {e}")
                traceback.print_exception(type(e), e, e.__traceback__)
            response = "Sorry, something went wrong."



        message_placeholder.markdown(response) 
        st.session_state.messages.append(AIMessage(response))
