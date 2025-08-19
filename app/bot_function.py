import os
import re
from openai import OpenAI
from dotenv import load_dotenv
from RAG_function import record_text_extraction, embed_chunks
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import FAISS


def bot_call(test_doc_path):
    load_dotenv()
    key_ct = os.environ["OPENAI_API_KEY"]
    client = OpenAI(api_key=key_ct)

    test_text_chunks = record_text_extraction(test_doc_path)
    embeddings = embed_chunks(test_text_chunks, 1500, 250, test_doc_path)

    ### RETRIEVING EMBEDDINGS
    chunks_to_analize = 5
    vs = FAISS.load_local(
        "faiss_index", embeddings, allow_dangerous_deserialization=True
    )
    retriever = vs.as_retriever(search_kwargs={"k": chunks_to_analize})

    ### BUILDING THE MODEL
    model = "gpt-5-nano"
    # model = "gpt-4o-mini"

    llm = ChatOpenAI(
        model=model,
        # temperature=0.5,
        # max_tokens=250,
        timeout=None,
        max_retries=2,
    )

    ### BUILDING PROMPT TEMPLATE
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """Responde a la siguiente pregunta usando el contexto y la historia previa de la conversacion.
                Si no estas seguro de que el contexto responde a la pregunta, responde: La informacion
                no se encuentra en el documento
                Contexto {context}
                """,
            ),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
        ],
    )

    ### CREATING CHAT MEMORY
    memory = ConversationBufferMemory(
        memory_key="chat_history", input_key="input", return_messages=True
    )

    ### CREATING CHAT OBJECT
    chat = LLMChain(llm=llm, prompt=prompt, memory=memory)

    return retriever, chat
