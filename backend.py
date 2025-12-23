from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, SystemMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph.message import add_messages
from document_store import load_resume

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2,
    streaming=True
)

resume_db = load_resume("resume.pdf")

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state: ChatState):
    messages = state["messages"]
    question = messages[-1].content

    docs = resume_db.similarity_search(question, k=4)

    context = "\n\n".join(doc.page_content for doc in docs)

    system_prompt = SystemMessage(
    content=(
        "You are a friendly AI assistant.\n\n"
        "Rules:\n"
        "1. If the user greets you or makes small talk (e.g. 'hello', 'hi', 'how are you'), respond normally.\n"
        "2. If the user asks about their profile, skills, experience, or background, answer ONLY using the resume.\n"
        "3. If the information is not in the resume, clearly say you don't have that information.\n\n"
        f"RESUME CONTENT:\n{context}"
    )
)


    response = llm.invoke([system_prompt] + messages)
    return {"messages": [response]}

checkpointer = MemorySaver()

graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer=checkpointer)
