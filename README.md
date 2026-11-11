# MemoryBot AI – Local LLM Chatbot with LangChain Memory

## Project Description

MemoryBot AI is a simple chatbot application built using Python, Streamlit, LangChain, and Ollama. It uses a locally running Large Language Model (LLM) to answer user questions and maintain conversation history.

The chatbot remembers previous messages within the same chat session and provides relevant responses based on the conversation.

## Objectives

- Build a simple chatbot using a local LLM.
- Integrate LangChain for chatbot functionality.
- Implement conversation memory.
- Maintain previous user and AI messages.
- Provide an interactive user interface using Streamlit.

## Technologies Used

- **Python** – Programming language
- **Streamlit** – User interface
- **LangChain** – LLM framework
- **Ollama** – Local LLM runtime
- **Qwen 2.5 (1.5B)** – Language model
- **InMemoryChatMessageHistory** – Conversation history storage

## Features

1. Interactive chatbot interface.
2. Local LLM integration.
3. Conversation memory using LangChain.
4. Supports Tamil and English conversations.
5. Remembers previous messages in the current session.
6. Clear Chat option to start a new conversation.
7. No paid API key required.

## Project Structure

```text
MemoryBot AI/
│
├── memory.py
├── reqy.txt
├── README.md
└── .venv/
```

## Installation

### Step 1: Install Python

Install Python 3.12 or a compatible version.

### Step 2: Install Ollama

Download and install Ollama from:

https://ollama.com/download

### Step 3: Download the AI Model

```bash
ollama pull qwen2.5:1.5b-instruct
```

### Step 4: Install Required Libraries

```bash
pip install -r reqy.txt
```

### Step 5: Run the Application

```bash
python -m streamlit run memory.py
```

## How It Works

1. The user enters a message in the chatbot.
2. The message is passed to the LangChain chatbot.
3. The local Qwen model processes the input.
4. LangChain retrieves the previous conversation history.
5. The AI generates a response using the conversation context.
6. The conversation is stored in memory for future messages in the same session.

## Expected Output

The chatbot responds to user questions and remembers previously shared information during the current session.

**Example:**

User: My favourite colour is blue.

AI: That's nice!

User: What is my favourite colour?

AI: Your favourite colour is blue.

## DEMO
## Screenshot

<img width="1920" height="1080" alt="Screenshot (208)" src="https://github.com/user-attachments/assets/149887fb-37d6-44be-858b-f6fd35364184" />

<img width="1920" height="1080" alt="Screenshot (209)" src="https://github.com/user-attachments/assets/3efaccbe-a45c-4100-9026-ce5ab11e9a71" />

<img width="1920" height="1080" alt="Screenshot (210)" src="https://github.com/user-attachments/assets/ab3eea30-f5e2-4b6b-a4c9-a5df81a80d00" />


## Limitations

- Requires Ollama to be installed and running.
- Requires the AI model to be downloaded.
- Conversation memory is temporary and stored in application memory.
- Chat history is not permanently saved after the session is reset.

## Conclusion

MemoryBot AI demonstrates how a local Large Language Model can be integrated with LangChain memory to create an interactive chatbot. It provides a simple way to understand local LLM integration and conversational memory without depending on paid cloud APIs.
