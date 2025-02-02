import re

def format_markdown(text):
    """Convert OCR-extracted text into Markdown format."""
    
    # Convert headers (detect single-line headings)
    text = re.sub(r'^\s*(\w+.*)\s*$', r'# \1', text, flags=re.MULTILINE)
    
    # Convert bullet points (- item)
    text = re.sub(r'^\s*-+\s*(.*)', r'- \1', text, flags=re.MULTILINE)
    
    # Convert numbered lists (1. item)
    text = re.sub(r'^\s*\d+\.\s*(.*)', r'1. \1', text, flags=re.MULTILINE)
    
    return text

# Example usage
if __name__ == "__main__":
    raw_text = "Meeting Notes\n- Discuss project goals\n1. Research AI models\n2. Implement OCR"
    markdown_text = format_markdown(raw_text)
    print(markdown_text)
