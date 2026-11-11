
import streamlit as st
import uuid

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory


st.set_page_config(
    page_title="MemoryBot AI",
    page_icon="🤖",
    layout="centered"
)

store = {}


def get_session_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()

    return store[session_id]


@st.cache_resource
def create_chatbot():

    llm = ChatOllama(
        model="qwen2.5:1.5b-instruct",
        temperature=0.3
    )

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are MemoryBot AI, a helpful chatbot. "
            "Remember the conversation history provided to you. "
            "Answer in the same language as the user's message "
            "when possible. Be friendly and clear."
        ),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{question}")
    ])

    chain = prompt | llm

    chatbot = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="question",
        history_messages_key="history"
    )

    return chatbot


if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []


st.title("🤖 MemoryBot AI")

st.subheader("Local LLM Chatbot with LangChain Memory")

st.write(
    "Chat with your local AI assistant. "
    "It remembers your previous messages in this conversation."
)

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.session_state.session_id = str(uuid.uuid4())
    st.rerun()


for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


user_input = st.chat_input("Type your message here...")

if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    try:

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                chatbot = create_chatbot()

                response = chatbot.invoke(
                    {"question": user_input},
                    config={
                        "configurable": {
                            "session_id": st.session_state.session_id
                        }
                    }
                )

                answer = response.content

                st.markdown(answer)

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

    except Exception as e:

        st.error(
            "Unable to connect to the local model. "
            "Please check whether Ollama is running "
            "and the model is installed."
        )

        st.caption(str(e))


st.divider()

st.caption(
    "Python | Streamlit | LangChain | Ollama"
)
