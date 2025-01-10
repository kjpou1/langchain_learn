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
 
---
       
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


---


## RAG Pipeline


[Video Link](https://www.youtube.com/watch?v=9Thc6hRw2Gs&list=PLA1lVIthbM1D5I6r5uY2K89X1KD2w5LNh&index=9)

### Project Overview

This project demonstrates how to build a **Retrieval-Augmented Generation (RAG) pipeline** using [LangChain](https://github.com/hwchase17/langchain) and popular vector databases such as **ChromaDB** and **FAISS**. It walks you through:

1. **Data Ingestion**  
   - Loading various file formats (PDF, text, web pages) using LangChain’s document loaders.

2. **Text Splitting (Transform)**  
   - Breaking larger documents into manageable chunks that fit LLM context windows.

3. **Embedding**  
   - Converting text chunks into vector representations (e.g., using OpenAI Embeddings or Ollama).

4. **Vector Store**  
   - Storing embeddings in a specialized database (ChromaDB, FAISS) for efficient similarity search.

5. **Query & Retrieval**  
   - Executing similarity searches to find the most relevant text chunks for a given user query.

By the end, you’ll have a working RAG pipeline that retrieves domain-specific context from your own documents, enriching LLM responses with accurate and up-to-date information. This approach is essential for building scalable, knowledge-intensive AI applications like specialized chatbots, search engines, or custom Q&A systems.


---

This notebook focuses on building an advanced Retriever and Chain implementation with LangChain, allowing for efficient retrieval of relevant information and interaction with large language models (LLMs). Below is a summary for your project README file:

---

## Advanced Retriever and Chain with LangChain

[Video Link](https://www.youtube.com/watch?v=tIwi92nkcu0&list=PLA1lVIthbM1D5I6r5uY2K89X1KD2w5LNh&index=10)

This notebook demonstrates the construction of a Retrieval-Augmented Generation (RAG) pipeline that integrates LangChain's Retriever and Chain components with OpenAI and Ollama LLMs for advanced Q&A functionalities.

### Key Features:
1. **Environment Configuration:**
   - Uses environment variables for dynamic configuration, including API base URLs and model specifications.

2. **Document Loading:**
   - Supports multiple formats via LangChain's community document loaders.
   - Examples include loading PDFs, text files, and web content.

3. **Data Processing:**
   - Converts loaded documents into embeddings using vectorization techniques (OpenAI embeddings or other embeddings).
   - Stores processed embeddings in vector databases like FAISS or Chroma.

4. **Retriever Implementation:**
   - Connects the vector database to a Retriever interface, enabling efficient query handling.

5. **Chain Construction:**
   - Leverages LangChain's `create_stuff_document_chain` to format retrieved documents into context for LLMs.
   - Customizable prompts enhance interaction and context utilization.

6. **Advanced Q&A Functionality:**
   - Combines Retriever and Chain to create a responsive Q&A pipeline.
   - Handles user queries by retrieving relevant documents and generating detailed answers.

### Use Cases:
- Knowledge management systems.
- Interactive chatbots powered by domain-specific data.
- Retrieval-based summarization and Q&A.

### Requirements:
- Python with LangChain, FAISS, Chroma, and OpenAI embeddings.
- Ollama setup for model interaction (local or cloud-hosted).

