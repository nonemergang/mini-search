from analyzer import analyze_document
from document import Document
index = {}

def index_document(document: Document):
    words = analyze_document(document.text)
    for word in words:
        if word not in index:
            index[word] = set()
        index[word].add(document.doc_id)