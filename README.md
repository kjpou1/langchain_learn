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
        
## FastAPI + LangServe Integration

[Video Link](https://www.youtube.com/watch?v=XWB5DXP-DO8&list=PLA1lVIthbM1D5I6r5uY2K89X1KD2w5LNh&index=6)
Use FastAPI for serving LangChain-based LLM endpoints, allowing your front-end (or other services) to invoke specific prompts/models via REST APIs.


### Command Lines to Run the App and Client

1. **Start the FastAPI Server**
   ```bash
   cd API
   python app.py
   ```
   - Server will listen on port `8000` by default.  
   - Swagger docs available at: `http://127.0.0.1:8000/docs`

2. **Run the Client (Streamlit App)**
   ```bash
   streamlit run client.py
   ```
   - This front-end will call the FastAPI routes, showcasing how to consume the LLM endpoints in your UI.  