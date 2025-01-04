import os

import streamlit as st
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Load environment variables from .env file
load_dotenv()

# Retrieve the OPENAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set in the .env file")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Retrieve the LANGCHAIN API key
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")

if not LANGCHAIN_API_KEY:
    raise ValueError("LANGCHAIN_API_KEY is not set in the .env file")

os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY
## Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"


## Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant.  Please respond to the user queries."),
        ("user", "Question: {question}"),
    ]
)

## streamlit framework

st.title("Langchain Demo with OPENAI API")
input_text = st.text_input("Search the topic u want")

# openAI LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))
