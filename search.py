from analyzer import analyze_document
from index import index


def and_search(query: str) -> set:
    terms = analyze_document(query)

    if not terms:
        return set()

    result = index.get(terms[0], set()).copy()

    for term in terms[1:]:
        result.intersection_update(index.get(term, set()))

    return result
