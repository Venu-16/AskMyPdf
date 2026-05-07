import tempfile

import streamlit as st

from utils.Embeddings import get_embeddings
from utils.Retriver import retrieve_docs
from utils.TextSplitter import split_text
from utils.documentloader import load_pdf
from utils.vectoreStore import create_vector_store


def load_and_index_pdf(uploaded_file):
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
        tmp.write(uploaded_file.getbuffer())
        tmp_path = tmp.name

    docs = load_pdf(tmp_path)
    chunks = split_text(docs)
    embeddings = get_embeddings()
    vector_store = create_vector_store(chunks, embeddings)
    return vector_store


def main():
    st.title("AskMyPdf")
    st.write("Upload a PDF and ask questions about its content.")

    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

    if uploaded_file is not None:
        if (
            "vector_store" not in st.session_state
            or st.session_state.get("uploaded_file_name") != uploaded_file.name
        ):
            with st.spinner("Indexing PDF, this may take a moment..."):
                st.session_state.vector_store = load_and_index_pdf(uploaded_file)
                st.session_state.uploaded_file_name = uploaded_file.name

        query = st.text_input("Ask a question")

        if query:
            with st.spinner("Searching for relevant passages..."):
                docs = retrieve_docs(st.session_state.vector_store, query)

            if docs:
                for idx, doc in enumerate(docs, start=1):
                    st.markdown(f"### Result {idx}")
                    st.write(doc.page_content)
                    if doc.metadata:
                        st.caption(f"Metadata: {doc.metadata}")
            else:
                st.warning("No relevant content found. Try a different question.")

    else:
        st.info("Upload a PDF to begin.")


if __name__ == "__main__":
    main()
