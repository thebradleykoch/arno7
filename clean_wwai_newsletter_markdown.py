import re
import os
import html
import urllib.parse

# Specify the input and output folders at the beginning for easy modification
input_folder = '/Users/bradleykoch/Downloads/WWAI Newsletters (Markdownload Raw Source)'
output_folder = '/Users/bradleykoch/Obsidian/NeuroBlade (Remote)/Eternal Creator OS/AI OS/Arno7/03 Components/02 Knowledge Base/Knowledge Base Files/Resource Layer/Framework Context Sources/WWAI Newsletters'


def clean_newsletter_content(content):
    # This function cleans the newsletters using Regex
    cleaned_content = re.sub(
        r'<merlin-component[^>]*></merlin-component>', r'', content)
    cleaned_content = re.sub(
        r'(```\n?)?(<code>){1,}(\n?)', r'```\n', cleaned_content)
    cleaned_content = re.sub(
        r'(\n?)(</code>){1,}(\n?```)?', r'\n```', cleaned_content)
    cleaned_content = re.sub(
        r'(#+\s*)(.*?)(\*\*)(.+?)(\*\*)(.*?)', r'\1\2\4\6', cleaned_content)
    cleaned_content = re.sub(r'\n-\s{2,}', r'\n- ', cleaned_content)
    cleaned_content = re.sub(r'(\n\d{1,2}\.)\s{2,}', r'\1 ', cleaned_content)
    cleaned_content = re.sub(
        r'\[\s*\n*\s*!\[\]\((.*?)\)\s*\n*\s*\]\(.*?\)', r'![](\1)', cleaned_content)
    cleaned_content = re.sub(
        r'(-*)\s*(!\[\]\(.*?\))', r'\1\n\n\2', cleaned_content)
    cleaned_content = re.sub(
        r'(“|”)', r'"', cleaned_content)
    cleaned_content = re.sub(
        r'```(?=\n[^\n])', r'```markdown', cleaned_content)
    # This line fixes any HTML entity substitutions
    cleaned_content = html.unescape(cleaned_content)
    return cleaned_content


def process_single_file(filepath, output_folder):
    # This function processes a single file
    with open(filepath, 'r', encoding='utf-8') as file:
        original_content = file.read()
    # Clean the content
    cleaned_content = clean_newsletter_content(original_content)

    # Construct the new file path in the output directory
    filename = os.path.basename(filepath)
    new_filepath = os.path.join(output_folder, filename)

    # Write the cleaned content to a new file
    with open(new_filepath, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)

    # Create and print a clickable link in VS Code terminal
    url_encoded_path = urllib.parse.quote(new_filepath)
    clickable_url = f"file://{url_encoded_path}"
    print(f"Cleaned content written to: {clickable_url}")


def batch_process_folder(input_folder, output_folder):
    # This function batch processes all Markdown files in the input directory
    for filename in os.listdir(input_folder):
        if filename.endswith(".md"):  # Checks if the file is a Markdown file
            filepath = os.path.join(input_folder, filename)
            process_single_file(filepath, output_folder)

    # Create and print a clickable link in VS Code terminal
    url_encoded_path = urllib.parse.quote(output_folder)
    clickable_url = f"file://{url_encoded_path}"
    print(f"Cleaned content written to: {clickable_url}")


# Main function to run

def main():
    # For batch processing, call batch_process_folder
    # For single file processing, call process_single_file with the specific file path

    # Uncomment one line or the other below (choose between batch processing & single-file processing)

    batch_process_folder(input_folder, output_folder)
    # process_single_file(input_folder, output_folder)


if __name__ == "__main__":
    # This function ensures the code is only executed if it's run directly (so this script won't run if it's just being imported by another module)
    main()
