import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

# from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

# from langchain_community.llms import Ollama
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langserve import add_routes

# Load environment variables from .env file
load_dotenv()

# Retrieve the OPENAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set in the .env file")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Retrieve the OPENAI API key
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
print(f"OLLAMA base url: {OLLAMA_BASE_URL}")

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")

if not OLLAMA_MODEL:
    raise ValueError("OLLAMA_MODEL is not set in the .env file")

print(f"OLLAMA model: {OLLAMA_MODEL}")

app = FastAPI(title="Lanchain Server", version="1.0", description="A simple API Server")

add_routes(app, ChatOpenAI(), path="/openai")
model = ChatOpenAI()
# ollama  LLM
llm = ChatOllama(base_url=OLLAMA_BASE_URL, model=OLLAMA_MODEL)

prompt1 = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} with 100 words."
)
prompt2 = ChatPromptTemplate.from_template(
    "Write me a poem about {topic} for a 5 year old child."
)

add_routes(app, prompt1 | model, path="/essay")

add_routes(app, prompt2 | llm, path="/poem")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
