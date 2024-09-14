import re

def clean_text(text):
    # Remove special characters and normalize text
    text = re.sub(r'\W+', ' ', text)
    sections = {
        "economy": extract_section(text, "economy"),
        "healthcare": extract_section(text, "healthcare")
    }
    return sections

def extract_section(text, keyword):
    # Simple keyword-based section extraction
    if keyword in text.lower():
        return f"Information on {keyword}."
    return "Not found"
