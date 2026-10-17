import streamlit as st
from core.router import Router
from core.memory import Memory
from handlers.explain import ExplainHandler
from handlers.generate import GenerateHandler

st.set_page_config(page_title="Coding Assistant", page_icon="assets/icon.png")
st.title("Intelligent AI Coding Assistant")


@st.cache_resource
def build_router() -> Router:
    return Router({"explain": ExplainHandler(), "generate": GenerateHandler()})


router = build_router()

if "memory" not in st.session_state:
    st.session_state.memory = Memory()
    
memory: Memory = st.session_state.memory


with st.sidebar:
    
    if st.button("Clear conversation"):
        memory.clear()
        st.rerun()
        
    with st.expander(f"({len(memory.get_history())} messages sent to LLM)"):
        for m in memory.get_history():
            st.markdown(f"**{m.type}:** {m.content[:80]}...")


for m in memory.messages:
    with st.chat_message("user" if m.type == "human" else "assistant"):
        st.markdown(m.content)


if query := st.chat_input("Welcome, how can I help you, sir?"):
    
    with st.chat_message("user"):
        st.markdown(query)
        
    with st.chat_message("assistant"):
        try:
            with st.spinner("Thinking..."): 
                intent, stream = router.route_stream(query, memory.get_history())
                first = next(stream, "") 

            def full_stream():
                yield first
                yield from stream

            text = st.write_stream(full_stream())
            memory.add_user(query)
            memory.add_ai(text)
        except Exception as e:
            st.exception(e)