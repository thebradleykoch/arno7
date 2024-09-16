# Chunked Text Title Maker

import os
import glob

def format_file_title(file_path, title, output_folder):
    with open(file_path, 'r') as file:  # Open the file for reading
        content = file.readlines()  # Read all lines in the file

        # If the title is already the first line but without the markdown '#', update it
        if content and content[0].strip() == title:
            content[0] = f'# {title}\n'
        # If the title is not there, insert it
        elif not content or title not in content[0]:
            content.insert(0, f'# {title}\n\n')

    # Determine the new file path in the output folder
    new_file_path = os.path.join(output_folder, os.path.basename(file_path))
    with open(new_file_path, 'w') as file:  # Open the file for writing
        file.writelines(content)  # Write the updated content

def get_next_chunk_folder(base_dir):
    i = 1
    while True:
        chunk_folder = os.path.join(base_dir, f'Chunked Text {i}')
        if not os.path.exists(chunk_folder):
            os.makedirs(chunk_folder)  # Create the folder if it doesn't exist
            return chunk_folder
        i += 1  # Increment i until we find a new folder name

# This is your base directory where all the files are
base_dir = '/Users/bradleykoch/Library/Mobile Documents/com~apple~CloudDocs/Copywriting/Clients/Course Modules/01 Beginner Section - JavaScript Simplified Transcripts/TXT Files'

# Let's grab all the '.txt' files from the directory
text_files = glob.glob(os.path.join(base_dir, '*.txt'))

# Get the new folder to save updated files
output_folder = get_next_chunk_folder(base_dir)

# Loop through the files and update them
for file_path in text_files:
    file_name = os.path.basename(file_path)  # Get the file name from the path
    title = file_name.replace('.txt', '')  # Remove the extension for the title
    format_file_title(file_path, title, output_folder)  # Call our formatting function with the new output folder