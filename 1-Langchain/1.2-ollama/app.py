import os
from dotenv import load_dotenv

load_dotenv()

from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

## Prompt Template
prompt=ChatPromptTemplate.from_messages([
    ("system", "you are a helpful assistant. please respond to the question asked"),
    ("user","Question:{question}")
])

## streamlit framework
st.title("Langchain Demo with Gemma:2b Model")
input_text=st.text_input("what question you have in mind?")

## instantiating Ollama LLM
llm=OllamaLLM(model="gemma:2b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser
if input_text:
    st.write(chain.invoke({"question":input_text}))