# langchain_learn
Learning Langchain for Generative AI



## chatbot

[Video Link](https://www.youtube.com/watch?v=5CJA1Hbutqc&list=PLA1lVIthbM1D5I6r5uY2K89X1KD2w5LNh&index=5)
In this example, we demonstrate how to build a simple chatbot using LangChain with both a paid LLM (OpenAI) and an open-source LLM (Llama 2 via Ollama). We walk through setting up prompts, integrating with Streamlit for a user interface, and tracking all LLM calls in real time using LangSmith’s observability dashboard. This approach allows you to seamlessly switch between different models while keeping the rest of your code and logic consistent.

### Running project files

#### OpenAI ollama chatbot
```bash
    streamlit run chatbot/app.py
```    


#### Local ollama chatbot
```bash
    streamlit run chatbot/localama.py
```    
        
