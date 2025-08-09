# LangChain Applications

A curated set of **LangChain-based prototypes** leveraging the power of **generative AI** and advanced query tools (e.g., **Groq**).  
Ideal for exploring integrations and showcasing **LLM-powered workflows**.

---

## 📂 Contents

- **`1-Langchain/`** — Sample LangChain implementations such as chaining models, prompt workflows, and retrieval-augmented generation (RAG).
- **`2-Groq/`** — Proof-of-concept applications that integrate Groq-style query logic or vector-based search capabilities.
- **`.env`** — Configuration placeholder for managing environment variables like API keys and model endpoints.
- **`requirements.txt`** — Lists dependencies essential for running the projects.
- **`README.md`** — (This file) Guide for developers to understand, run, and extend the applications.

---

## 🛠 Prerequisites

- **Python 3.8+**
- **API access credentials** (e.g., OpenAI API key) configured in `.env`
- **Virtual environment** (recommended) for dependency isolation

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/mvkrsna/Langchain-applications.git
cd Langchain-applications

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env        # Then edit .env with your credentials
