import os

# Define your input and output paths
input_path = '/Users/bradleykoch/Library/Mobile Documents/com~apple~CloudDocs/Copywriting/Clients/Course Modules/02 Advanced Section - JavaScript Simplified Transcripts/TXT'
output_path = '/Users/bradleykoch/Library/Mobile Documents/com~apple~CloudDocs/Copywriting/Clients/Course Modules/02 Advanced Section - JavaScript Simplified Transcripts/MD'

# Ensure the output directory exists, if not, create it
os.makedirs(output_path, exist_ok=True)

# Loop through each file in the input directory
for filename in os.listdir(input_path):
    # Check if the file is a .txt file
    if filename.endswith('.txt'):
        # Construct the full path of the file
        file_path = os.path.join(input_path, filename)

        # Open and read the contents of the txt file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.readlines()

        # Prepare the markdown formatted title
        # Extract the file name without the extension for the heading
        title = os.path.splitext(filename)[0]
        # Adding three newlines as requested
        markdown_title = f"# {title}\n\n\n"

        # Check and handle the special case where content starts with "- "
        if content[0].startswith('- '):
            content[0] = content[0][2:]  # Remove the dash and space

        # If the first line of content is the file name, replace it with the markdown title
        if content[0].strip() == title:
            content[0] = markdown_title
        else:
            # Otherwise, prepend the markdown title to the content
            content.insert(0, markdown_title)

        # Construct the output file path with the .md extension
        output_file_path = os.path.join(output_path, f"{title}.md")

        # Write the modified content to a new .md file in the output directory
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.writelines(content)
