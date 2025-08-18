import os
from app.RAG_function import get_pdf_paths


def test_import_pdfs() -> None:
    """Test for the import function"""
    home_directory = os.getcwd()
    partial_folder_path = "data/raw-pdfs"
    complete_folder_path = os.path.join(home_directory, partial_folder_path)

    pdf_names = [
        "Acta Sesión Conmemorativa  No. 064 2024-05-24.pdf",
        "Acta Sesión Extraordinaria  No. 052 2024-03-08.pdf",
        "Acta Sesión Ordinaria  No. 056 2024-04-09.pdf",
    ]

    correct_pdf_paths = [
        os.path.abspath(os.path.join(complete_folder_path, f)) for f in pdf_names
    ]

    assert sorted(get_pdf_paths(partial_folder_path)) == sorted(correct_pdf_paths)
