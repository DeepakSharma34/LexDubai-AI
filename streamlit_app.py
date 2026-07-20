import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/api/chat"

st.set_page_config(
    page_title="LexDubai AI",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ LexDubai AI")
st.sidebar.markdown("""
### About

LexDubai AI is a Retrieval-Augmented Generation (RAG) chatbot for UAE Employment Law.

### Tech Stack

- FastAPI
- Streamlit
- Gemini 2.5 Flash
- Qdrant
- FastEmbed
- Python
""")
st.caption("UAE Employment Law Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message["role"] == "assistant" and message.get("sources"):
            with st.expander("📚 Sources"):
                for source in message["sources"]:
                    st.write(
                        f"Article {source['article']} | Page {source['page']}"
                    )
if not st.session_state.messages:
    st.info(
        "👋 Welcome! Ask any question related to UAE Employment Law."
    )
prompt = st.chat_input("Ask a legal question...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Searching UAE Employment Law..."):

            try:
                response = requests.post(
                    API_URL,
                    json={"question": prompt},
                    timeout=60
                )

                response.raise_for_status()

                data = response.json()

            except Exception as e:
                st.error(f"Error: {e}")
                st.stop()

            st.markdown(data["answer"])

            with st.expander("📚 Sources"):

                for source in data["sources"]:

                    st.write(
                        f"Article {source['article']} | Page {source['page']}"
                    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": data["answer"],
            "sources": data["sources"]
        }
    )

st.sidebar.title("LexDubai AI")

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.messages = []
    st.rerun()