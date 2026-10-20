# tools/knowledge_tools.py
# Knowledge Agent tool - reads directly from text files, no ollama/chromadb needed

import os

# Locate data directory
_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")


def _load_file(filename: str) -> str:
    """Load a text file from the data directory."""
    try:
        with open(os.path.join(_DATA_DIR, filename), "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"[Error loading {filename}: {e}]"


def search_knowledge(query: str) -> str:
    """
    Search TechCorp company policies and FAQs to answer any employee question.
    Searches both company_policies.txt and company_faqs.txt and returns
    all relevant sections. Call this tool ONCE per question.

    Args:
        query: The question or topic to search for
               (e.g. 'working hours', 'leave policy', 'dress code')

    Returns:
        A complete answer string with all relevant information found.
    """
    query_lower = query.lower()
    keywords = [w for w in query_lower.replace("?", "").replace(",", "").split() if len(w) > 2]

    policies_text = _load_file("company_policies.txt")
    faqs_text     = _load_file("company_faqs.txt")

    results = []

    # Search policies by paragraph/section
    for source_name, text in [("Company Policy", policies_text), ("Company FAQ", faqs_text)]:
        # Split into sections by double newline
        sections = [s.strip() for s in text.split("\n\n") if s.strip()]
        for section in sections:
            section_lower = section.lower()
            # Score: how many keywords appear in this section
            score = sum(1 for kw in keywords if kw in section_lower)
            if score > 0:
                results.append((score, source_name, section))

    if not results:
        # Fallback: return full content of both files
        return (
            f"=== Company Policies ===\n{policies_text}\n\n"
            f"=== Company FAQs ===\n{faqs_text}"
        )

    # Sort by relevance score (highest first), take top 4
    results.sort(key=lambda x: x[0], reverse=True)
    top_results = results[:4]

    answer_parts = [f"Knowledge base results for '{query}':\n"]
    for i, (score, source, section) in enumerate(top_results, 1):
        answer_parts.append(f"[{source} {i}]\n{section}")

    return "\n\n".join(answer_parts)
