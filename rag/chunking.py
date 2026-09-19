from pathlib import Path
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_document(file_path: str):

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Document not found: {file_path}"
        )

    if path.suffix.lower() == ".pdf":

        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    elif path.suffix.lower() == ".txt":

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:
            text = file.read()

    else:
        raise ValueError(
            "Only PDF and TXT files are supported."
        )

    if not text.strip():
        raise ValueError(
            "No readable text found in the document."
        )

    return text


def load_and_chunk(file_path: str):

    text = load_document(file_path)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = splitter.split_text(text)

    print(f"Document characters: {len(text)}")
    print(f"Chunks created: {len(chunks)}")

    return chunks