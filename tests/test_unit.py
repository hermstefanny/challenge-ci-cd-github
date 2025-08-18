from app.RAG_function import get_pdf_paths


def test_import_pdfs() -> None:
    """Test for the import function"""
    correct_pdf_paths = [
        "C:\\Users\\herms\\Desktop\\BeCode-Bauman\\TheMountain_Projects\\challenge-ci-cd-github\\data\\raw-pdfs\\Acta Sesión Conmemorativa  No. 064 2024-05-24.pdf",
        "C:\\Users\\herms\\Desktop\\BeCode-Bauman\\TheMountain_Projects\\challenge-ci-cd-github\\data\\raw-pdfs\\Acta Sesión Extraordinaria  No. 052 2024-03-08.pdf",
        "C:\\Users\\herms\\Desktop\\BeCode-Bauman\\TheMountain_Projects\\challenge-ci-cd-github\\data\\raw-pdfs\\Acta Sesión Ordinaria  No. 056 2024-04-09.pdf",
    ]

    assert get_pdf_paths("data/raw-pdfs") == correct_pdf_paths
