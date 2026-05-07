def retrieve_docs(vectorstore, query):

    docs = vectorstore.similarity_search(
        query=query,
        k=3
    )

    return docs

