# Real-time-Voice-RAG
# 🎙️ Realtime Voice RAG System

An end-to-end **Real-Time Voice-enabled Retrieval-Augmented Generation (RAG)** system that allows users to query documentation and receive **intelligent answers with voice output**.

---

## 🚀 Features

* 🔎 **Document Crawling** using Firecrawl
* 🧠 **Semantic Search** powered by Qdrant Vector Database
* ⚡ **Fast Embeddings** using FastEmbed
* 🤖 **LLM-powered Responses** via OpenAI
* 🎤 **Text-to-Speech (TTS)** for voice responses
* ⚡ **Low-latency architecture** for near real-time interaction
* 📦 Modular backend with clean architecture

---

## 🏗️ Project Structure

```
RealtimeVoiceRAG/
│
├── backend/
│   └── app/
│       ├── main.py
│       ├── routes.py
│       ├── core/
│       │   └── config.py
│       ├── services/
│       │   ├── embedding.py
│       │   ├── ingestion.py
│       │   ├── retrieval.py
│       │   ├── qdrant_service.py
│       │   ├── llm_stream.py
│       │   ├── tts_stream.py
│       ├── utils/
│       │   └── chunking.py
│
├── frontend/
│   └── streamlit_app.py
│
├── scripts/
│   └── ingest.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

* **Backend:** FastAPI
* **Frontend:** Streamlit
* **Vector DB:** Qdrant
* **Embeddings:** FastEmbed
* **LLM & TTS:** OpenAI API
* **Crawler:** Firecrawl

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_openai_key
FIRECRAWL_API_KEY=your_firecrawl_key
QDRANT_URL=http://localhost:6333
```

---

## 🛠️ Installation

### 1. Clone the Repository

```
git clone https://github.com/your-username/realtime-voice-rag.git
cd realtime-voice-rag
```

---

### 2. Create Virtual Environment

```
python -m venv .venv
.venv\Scripts\activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## 🧱 Running the System

---

### ▶️ Step 1: Start Qdrant

```
docker run -p 6333:6333 qdrant/qdrant
```

---

### ▶️ Step 2: Ingest Documentation

```
python scripts/ingest.py
```

---

### ▶️ Step 3: Run Backend

```
cd backend
uvicorn app.main:app --reload
```

---

### ▶️ Step 4: Run Frontend

```
cd frontend
streamlit run streamlit_app.py
```

---

## 🔄 How It Works

1. **Crawling:** Firecrawl extracts documentation content
2. **Chunking:** Text is split into smaller segments
3. **Embedding:** FastEmbed converts text into vectors
4. **Storage:** Qdrant stores vectors for semantic search
5. **Querying:** User query is embedded and matched
6. **LLM Processing:** OpenAI generates contextual answers
7. **Voice Output:** TTS converts response to speech

---

## ⚡ Performance Optimizations

* Async processing for faster response time
* Streaming LLM responses
* Efficient chunking strategy
* Lightweight embedding model (FastEmbed)

---

## 📌 Future Improvements

* 🎤 Real-time microphone input
* 🔊 Streaming voice responses
* 🧠 Conversation memory
* 🌐 Multi-document ingestion
* 📊 Analytics dashboard

---

## 🤝 Contributing

Pull requests are welcome! Feel free to open issues for suggestions or improvements.

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

* OpenAI
* Qdrant
* Firecrawl
* FastEmbed

---

## ⭐ Support

If you found this project helpful, please ⭐ the repo!
