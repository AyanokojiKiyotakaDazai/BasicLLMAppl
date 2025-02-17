import os
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["LANGSMITH_TRACKING_V2"] = "true"
os.environ["LANGSMITH_PROJECT"] = os.getenv("LANGSMITH_PROJECT")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an assistant. Give proper resposes"),
        ("user","{question}")
    ]
)
st.title("Chat With Your Assistant")
input_txt = st.text_input("Enter the querry here")
llm = OllamaLLM(model = "gemma2:2b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser
if input_txt:
    response = st.write(chain.invoke({"question":input_txt}))
    st.write(response)
