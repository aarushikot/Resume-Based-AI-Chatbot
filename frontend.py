import streamlit as st
import uuid
from backend import chatbot
from langchain_core.messages import HumanMessage

st.set_page_config(
    page_title="Resume Chatbot",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "chats" not in st.session_state:
    st.session_state.chats = {}

if "current_thread" not in st.session_state:
    tid = str(uuid.uuid4())
    st.session_state.current_thread = tid
    st.session_state.chats[tid] = {
        "title": "New Chat",
        "messages": []
    }

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
with st.sidebar:
    st.title("💬 Chats")

    if st.button("➕ New Chat"):
        tid = str(uuid.uuid4())
        st.session_state.current_thread = tid
        st.session_state.chats[tid] = {
            "title": "New Chat",
            "messages": []
        }
        st.rerun()

    st.divider()

    for tid, chat in st.session_state.chats.items():
        if st.button(chat["title"], key=tid):
            st.session_state.current_thread = tid
            st.rerun()

# --------------------------------------------------
# MAIN CHAT
# --------------------------------------------------
current_chat = st.session_state.chats[st.session_state.current_thread]
messages = current_chat["messages"]

CONFIG = {"configurable": {"thread_id": st.session_state.current_thread}}

st.title("🤖 Resume Assistant")

# Show chat history
for msg in messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --------------------------------------------------
# INPUT
# --------------------------------------------------
user_input = st.chat_input("Ask something about your resume...")

if user_input:
    # ---- USER MESSAGE ----
    messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    if current_chat["title"] == "New Chat":
        current_chat["title"] = user_input[:30]

    # ---- ASSISTANT (STREAMING — CORRECT WAY) ----
    with st.chat_message("assistant"):
        ai_message = st.write_stream(
            message_chunk.content
            for message_chunk, metadata in chatbot.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode="messages"
            )
        )

    messages.append({"role": "assistant", "content": ai_message})
