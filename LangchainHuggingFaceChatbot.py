import os
import streamlit as st
from dotenv import load_dotenv
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceHub(repo_id="mistralai/Mistral-7B-Instruct-v0.3", model_kwargs={"temperature": 0.7})

prompt = PromptTemplate(
    input_variables=["query"],
    template="You are a helpful assistant. Answer the following question: {query}"
)

memory = ConversationBufferMemory()

chain_with_memory = LLMChain(llm=llm, prompt=prompt, memory=memory, output_parser=StrOutputParser())

st.set_page_config(page_title="Chatbot")

st.title("Chatbot with LangChain & Hugging Face Model")

st.sidebar.header("Instructions")
st.sidebar.markdown(
    """
    - Ask the chatbot any question.
    - The bot remembers the context of the conversation.
    - Type 'exit' to end the conversation.
    """
)

if "history" not in st.session_state:
    st.session_state.history = []

def get_response(user_input):
    if user_input.lower() == "exit":
        st.session_state.history.append({"user": user_input, "bot": "Goodbye!"})
        return "Goodbye!"

    bot_response = chain_with_memory.run(user_input)
    st.session_state.history.append({"user": user_input, "bot": bot_response})
    return bot_response

for message in st.session_state.history:
    if "user" in message:
        st.chat_message("user").markdown(f"**You:** {message['user']}")
    if "bot" in message:
        st.chat_message("assistant").markdown(f"**Bot:** {message['bot']}")

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Your message:", "")
    submit_button = st.form_submit_button("Send")

    if submit_button and user_input:
        response = get_response(user_input)
        st.chat_message("assistant").markdown(f"**Bot:** {response}")
