import os
import re
# Make sure this import matches how it's structured in your files
from markdownify import MarkdownConverter


# Regex cleanup function
def clean_up_md(md_content):
    # Existing cleanup operations
    # Trim whitespace at the start and end of each line
    # md_content = re.sub(r'^\s+|\s+$', '', md_content, flags=re.MULTILINE)
    # Replace 3+ blank lines with 2 blank lines
    md_content = re.sub(r'(\n\s*){3,}', '\n\n\n', md_content)
    # Example: Fixing bullet lists that might start without a newline
    # md_content = re.sub(r'([^\n])\n- ', r'\1\n\n- ', md_content)
    # Fixes mid-sentence line breaks
    md_content = re.sub(r'(.\s*)\n\s+?(\w)', r'\1 \2', md_content)

    return md_content


def convert_html_to_md(html_file_path, md_file_path):
    # Added encoding to handle any special characters in the file
    with open(html_file_path, 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()

    converter = MarkdownConverter()
    md_content = converter.convert(html_content)
    md_content = clean_up_md(md_content)
    with open(md_file_path, 'w', encoding='utf-8') as md_file:  # Create & write md file
        md_file.write(md_content)
    # Print clickable link to the file in VS Code terminal, encoding spaces for URL compatibility
    print(f"Markdown file saved: file://{md_file_path.replace(' ', '%20')}")


# Update these file paths to match yours
html_file_path = r"/Users/bradleykoch/Desktop/B-RAD/AI/ChatGPT/ARNO/Moms Project/Assignment Instructions/HTML/Linked Pages/Linked Page – Goals and Plans transcript.html"
md_file_path = r"/Users/bradleykoch/Desktop/B-RAD/AI/ChatGPT/ARNO/Moms Project/Assignment Instructions/MD/Linked Pages/Linked Page – Goals and Plans transcript.md"

convert_html_to_md(html_file_path, md_file_path)
