import os
import fitz
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.schema import Document
from langchain_community.vectorstores import FAISS


def get_pdf_paths(dir_name) -> list[str]:
    script_directory = os.getcwd()
    path_to_folder = os.path.join(script_directory, dir_name)

    pdf_paths = [
        os.path.abspath(os.path.join(path_to_folder, f))
        for f in os.listdir(path_to_folder)
        if f.lower().endswith(".pdf")
    ]

    return pdf_paths


def record_text_extraction(record_file_path) -> str:

    try:
        record_doc = fitz.open(record_file_path)
    except Exception:
        print("File path not found")
        return ""

    # Hard coded header and footer values according to layout document
    header_space = 0.165
    footer_space = 0.925

    record_text = ""

    for num_page in range(len(record_doc)):
        page = record_doc.load_page(num_page)

        page_height = page.rect.height
        page_width = page.rect.width

        text_rect = fitz.Rect(
            0, page_height * header_space, page_width, page_height * footer_space
        )

        page_text = page.get_text("text", clip=text_rect)

        record_text += page_text

    record_doc.close()

    return record_text


def chunk_splitting(doc, chunk_size, chunk_overlap):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    chunks = splitter.split_text(doc)

    return chunks


def embed_chunks(doc, chunk_size, chunk_overlap, doc_path):
    chunks = chunk_splitting(doc, chunk_size, chunk_overlap)
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small", openai_api_key=api_key
    )
    docs_to_embed = [
        Document(page_content=chunk, metadata={"source": os.path.basename(doc_path)})
        for chunk in chunks
    ]

    vs = FAISS.from_documents(docs_to_embed, embeddings)
    vs.save_local("faiss_index")
    print("FAISS index saved locally.")
    return embeddings
