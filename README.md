🤖 Resume-Based AI Chatbot (RAG)

This project is a resume-based AI chatbot built to explore how Retrieval-Augmented Generation (RAG) can be used to answer questions accurately and responsibly.

The core idea is simple:
If the information is not present in the resume, the chatbot should not guess.

💡 What This Project Does

The chatbot can:

Answer questions about my skills, education, and experience

Generate short summaries of my resume

Respond normally to greetings and casual questions

Clearly say “I don’t have that information” when details are not available (e.g., GPA, address, date of birth)

This helps demonstrate how hallucination-safe AI systems can be designed.

🛠️ Tech Stack

Python

LangChain

LangGraph (conversation state & memory)

ChromaDB (vector database)

OpenAI (LLM)

Streamlit (chat-style UI)

🧠 Why I Built This

I built this project to gain hands-on experience with:

RAG pipelines

Vector databases and embeddings

Managing conversation context

Designing guardrails to prevent hallucinations

Building simple, reliable AI applications

The focus was on correctness and trust, not just impressive outputs.
