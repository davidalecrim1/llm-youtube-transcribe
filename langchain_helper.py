from langchain_community.document_loaders import YoutubeLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

embeddings = OllamaEmbeddings(model="llama3.2:3b")
chat_history = []

def create_vector_db_from_youtube_url(url):
    transcript = _get_transcript_from_url(url)
    docs = _get_docs_from_transcript(transcript)

    db = FAISS.from_documents(docs, embedding=embeddings)
    return db

def _get_docs_from_transcript(transcript):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(transcript)
    return docs

def _get_transcript_from_url(url):
    loader = YoutubeLoader.from_youtube_url(url)
    transcript = loader.load()
    return transcript

def create_llama_model(model="llama3.2:3b"):
    return ChatOllama(model=model, temperature=0.3)

def create_chat_history():
    if chat_history == []:
        chat_history.append(
        ("system",f'''
        You are a helpful assistant that that can answer questions about youtube videos 
        based on the video's transcript.
            
        Only use the factual information from the transcript to answer the question.
        
        If you feel like you don't have enough information to answer the question, say "I don't know".
        
        Your answers should be verbose and detailed.
        ''')
        )

def append_chat_history(question, response):
    chat_history.append(("user", question))
    chat_history.append(("system", response))

def get_relevant_docs_based_on_question(db: FAISS, question, num_of_docs=5):
    relevante_docs = db.similarity_search(question, k=num_of_docs)
    docs_content = " ".join([doc.page_content for doc in relevante_docs])
    return docs_content

def create_user_question(question, docs_content):
    return (f"user", 
         f'''Answer the following question: ~~~{question}~~~ based on the video's transcript 
         relevant parts: ~~~{docs_content}~~~''')

def generate_response(llm: ChatOllama, db: FAISS, question, num_of_docs=5):
    docs_content = get_relevant_docs_based_on_question(db, question, num_of_docs)
    question = create_user_question(question, docs_content)
    response = llm.invoke(chat_history + [question])

    append_chat_history(question[1], response.content)
    return response
