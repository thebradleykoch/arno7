# Chunked Text File Merger

import os
import glob

# First, let's make a function that finds us a nice new home for our chunked files
def create_chunked_text_dir(base_path):
    dir_number = 1
    while True:
        new_dir = os.path.join(base_path, f"Chunked Text File Merger {dir_number}")
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
            return new_dir
        dir_number += 1

# The main stage: your file path where the party... I mean... the coding happens
base_directory = "/Users/bradleykoch/Library/Mobile Documents/com~apple~CloudDocs/Copywriting/Clients/Course Modules/01 Beginner Section - JavaScript Simplified Transcripts/TXT Files/Chunked Text 1"
chunked_text_directory = create_chunked_text_dir(base_directory)

# Initialize variables to store our text and count files
concatenated_text = ''
file_counter = 1

# Let's grab those .txt files, sorting them like we sort our vinyl collection
txt_files = sorted(glob.glob(os.path.join(base_directory, '*.txt')), key=lambda x: os.path.getmtime(x))

for txt_file in txt_files:
    with open(txt_file, 'r') as file:
        file_content = file.read()
        # If the next module is too big and we already have some content, time to cut and save
        if len(concatenated_text) + len(file_content) > 1500 and concatenated_text:
            chunk_filename = f'chunk_{file_counter}.txt'
            with open(os.path.join(chunked_text_directory, chunk_filename), 'w') as chunk_file:
                chunk_file.write(concatenated_text.strip())
            file_counter += 1
            concatenated_text = file_content  # Start with the next big module
        else:
            concatenated_text += file_content  # Pile up the next module

# After the loop, we gotta take care of the last straggler
if concatenated_text:
    chunk_filename = f'chunk_{file_counter}.txt'
    with open(os.path.join(chunked_text_directory, chunk_filename), 'w') as chunk_file:
        chunk_file.write(concatenated_text.strip())

print(f"Module files have been neatly chunked into {file_counter} files. Check 'em out in the 'Chunked Text' directory.")