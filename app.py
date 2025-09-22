from langchain_openai import ChatOpenAI #it help to interact with openai
from langchain_core.prompts import ChatPromptTemplate #chat prompt template to write chat
from langchain_core.output_parsers import StrOutputParser #use to display response which come from LLM model
from langchain_community.llms import Ollama # use with Ollama


import streamlit as st
import os # use to call all environment variable
from dotenv import load_dotenv  # use for ENV file

load_dotenv()

# environment variables call

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true" # for trace everything in langsmith account


## creating chatbot

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please provide response to the user queries"),
        ("user","Question:{question}")
    ]
) # this will guide how chatbot needs to work


# streamlit framework

st.title("Langchain Demo With LLAMA2 API")
input_text=st.text_input("Seach the topic you want")

# ollama LLAma2 LLm 
llm=Ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))

