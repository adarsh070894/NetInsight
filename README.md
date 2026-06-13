# Local AI Chatbot with Streamlit & Llama 3

A lightweight AI chatbot that runs completely locally using **Llama 3** through **Ollama** and provides an interactive web interface using **Streamlit**.

This project demonstrates how local Large Language Models (LLMs) can be integrated into applications without relying on cloud-based AI services.

---

## Features

* Runs completely locally (No cloud API required)
* Interactive chat interface built with Streamlit
* Session-based conversation history
* Uses locally hosted Llama 3 via Ollama
* Simple and lightweight architecture
* Easy to extend with APIs, tools, or automation workflows

---

## Architecture

```text
User
  │
  ▼
Streamlit Web UI
  │
  ▼
Ollama REST API
  │
  ▼
Llama 3 Model
  │
  ▼
AI Response
```

---

## Tech Stack

* Python
* Streamlit
* Ollama
* Llama 3

---

## Project Structure

```text
.
├── chatbot.py
├── requirements.txt
└── README.md
```

---

## Prerequisites

### Install Ollama

Download and install Ollama:

https://ollama.com

Verify installation:

```bash
ollama --version
```

### Pull the Llama 3 Model

```bash
ollama pull llama3
```

Start the Ollama service:

```bash
ollama serve
```

By default, Ollama runs on:

```text
http://localhost:11434
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install streamlit requests
```

---

## Running the Application

Start the chatbot:

```bash
streamlit run chatbot.py
```

The application will open in your browser automatically.

---

## Example Usage

User:

```text
What is OSPF?
```

Assistant:

```text
OSPF (Open Shortest Path First) is a link-state routing protocol used in IP networks...
```

---

## Learning Outcomes

This project helped in understanding:

* Local LLM deployment using Ollama
* REST API integration in Python
* Building conversational interfaces with Streamlit
* Managing session-based chat history
* Creating AI-powered applications without cloud dependencies

---

## Future Enhancements

* Network automation integration
* Device command execution
* Tool calling
* RAG (Retrieval-Augmented Generation)
* Multi-model support
* Chat history persistence
* Authentication and user management

---

## License

This project is open source and available under the MIT License.
