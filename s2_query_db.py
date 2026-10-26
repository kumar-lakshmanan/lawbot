from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory="legal_db",
    embedding_function=embedding
)

query = """
Person borrowed money and issued cheque.
Cheque bounced due to insufficient funds.
"""

docs = db.similarity_search(query, k=5)

for d in docs:
    print(d.page_content)