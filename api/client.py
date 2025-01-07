import requests
import streamlit as st


def get_openai_response(topic: str) -> str:
    url = "http://127.0.0.1:8000/essay/invoke"
    payload = {"input": {"topic": topic}}
    resp = requests.post(url, json=payload).json()
    return resp["output"]["content"]


def get_ollama_response(topic: str) -> str:
    url = "http://127.0.0.1:8000/poem/invoke"
    payload = {"input": {"topic": topic}}
    resp = requests.post(url, json=payload).json()
    return resp["output"]["content"]


st.title("LangChain LLM API Demo")

topic_essay = st.text_input("Write an essay on:")
if topic_essay:
    st.write(get_openai_response(topic_essay))

topic_poem = st.text_input("Write a poem on:")
if topic_poem:
    st.write(get_ollama_response(topic_poem))
