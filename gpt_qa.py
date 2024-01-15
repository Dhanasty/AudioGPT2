import os 
os.environ["OPENAI_API_KEY"] = "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"

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
def ask_question(content,qa):
    text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=500,
    chunk_overlap = 40,
    length_function = len,
    )
    texts = text_splitter.split_text(content)
    embeddings = OpenAIEmbeddings(openai_api_key="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")
    document_search= FAISS.from_texts(texts,embeddings)
    chain = load_qa_chain(OpenAI(),chain_type="stuff")
    query = qa
    docs = document_search.similarity_search(query)
    ans = chain.run(input_documents = docs,question=query)
    return ans

