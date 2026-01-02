# 🚀 AI-Powered Text Insight Engine

A full-stack web application that leverages **Natural Language Processing (NLP)** to analyze text data in real time.  
Designed with a modern **microservices architecture** and fully containerized using **Docker**.

---

## 🌟 Features

- **AI Text Analysis**
  - Named Entity Recognition (NER)
  - Sentence counting
  - Word and pattern analysis using SpaCy
- **High-Performance Backend**
  - Built with **FastAPI**
  - Asynchronous and highly efficient
- **Reactive Frontend**
  - Clean, responsive UI built with **React** and **Vite**
- **Containerized Architecture**
  - Fully managed with **Docker** and **Docker Compose**
  - Runs consistently on Linux, Windows, and macOS
- **Auto-generated API Documentation**
  - Interactive **Swagger UI** available out of the box

---

## 🛠 Tech Stack

### Backend
- Python 3.10
- FastAPI
- SpaCy (`en_core_web_sm`)

### Frontend
- React.js
- Vite
- Axios
- CSS3

### DevOps
- Docker
- Docker Compose
- `.dockerignore`

### Tools & Environment
- Linux-ready
- Git / GitLab flow

---

## 🚀 Getting Started (Run with Docker)

You don’t need to install Python or Node.js locally.  
You only need **Docker Desktop**.

### 1. Clone the repository

```bash
git clone https://github.com/Mahdieshn/Ai-Text-Analyzer.git
```

### 2. Launch the entire stack

```bash
docker-compose up --build
```

### 3. Access the application

- **Frontend:** http://localhost:5173  
- **Backend API Docs (Swagger):** http://localhost:8000/docs  

---

## 📁 Project Structure

```plaintext
├── backend/
│   ├── main.py          # FastAPI Logic & NLP Integration
│   ├── Dockerfile       # Python environment
│   └── requirements.txt # Project dependencies
├── frontend/
│   ├── src/             # React components
│   ├── Dockerfile       # Node.js environment
│   └── App.jsx          # Frontend Logic
└── docker-compose.yml   # Orchestration for both services
```

---

## 🧠 Why This Approach?

- **FastAPI** was chosen for its native support for **Pydantic validation** and high performance with AI models.
- **Docker Volumes** are used to allow real-time development without rebuilding containers.
- **CORS Middleware** is configured to ensure secure communication between the decoupled **Frontend** and **Backend** services.
