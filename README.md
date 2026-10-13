# AskMyPDF

A Streamlit application that lets users upload a PDF and search for relevant passages by asking questions.

## Architecture

![AskMyPDF Architecture](https://github.com/Venu-16/AskMyPdf/blob/main/askmyPdf%20Architechture.png)

## Workflow

1. Upload a PDF.
2. Extract and split the document text.
3. Generate embeddings and create a FAISS index.
4. Ask a question.
5. Retrieve relevant passages and display the results.

## Tech Stack

- Python
- Streamlit
- PDF loader
- Text splitter
- Embedding model
- FAISS

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```
