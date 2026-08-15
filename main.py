
from document import Document
from index import index_document, index
from search import and_search


doc_1 = Document(doc_id=1, text="This is the first document.")
doc_2 = Document(doc_id=2, text="This document is the second document.")
doc_3 = Document(doc_id=3, text="And this is the third one.")

index_document(doc_1)
index_document(doc_2)
index_document(doc_3)

print(index)
print(and_search("document second"))
print(and_search("document python"))
