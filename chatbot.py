from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
# from langchain import LLMChain
st. title("Sree's Chat Bot")
input_txt = st.text_input ("Please enter your queries here...")
prompt = ChatPromptTemplate.from_messages([("system", "you are a helpful AI assistant."), ("user", "user query: {query}")])

llm = Ollama (model="llama3.1")

output_parser = StrOutputParser()

chain = prompt|llm|output_parser

if input_txt:
  st.write(chain.invoke({"query":input_txt}))