# PSPDFKit API

import os
import requests
import json
from contextlib import contextmanager

def fetch_image_files(folder_path):
    """
    Given a folder path, this function returns a list of all files ending in .jpg or .png.
    """
    return [file_name for file_name in os.listdir(folder_path) if file_name.lower().endswith(('.jpg', '.png'))]

def build_request_payload(folder_path):
    image_files = fetch_image_files(folder_path)

    parts = [{'file': image_file} for image_file in image_files]
    
    with open_files(folder_path, image_files) as file_data:
        instructions = {
            'parts': parts,
            'actions': [{'type': 'ocr', 'language': 'english'}]
        }

        response = requests.request(
            'POST',
            'https://api.pspdfkit.com/build',
            headers={'Authorization': f'Bearer {API_KEY}'},  # Use the constant here
            files=file_data,
            data={'instructions': json.dumps(instructions)},
            stream=True
        )

        print("POSTED")
        
        if response.ok:
            with open('result.pdf', 'wb') as fd:
                for chunk in response.iter_content(chunk_size=8096):
                    fd.write(chunk)
        else:
            print(response.text)
            exit()

@contextmanager
def open_files(folder_path, image_files):
    """
    Context manager for handling the opening and closing of multiple files.
    """
    files = {image_file: open(os.path.join(folder_path, image_file), 'rb') for image_file in image_files}
    
    try:
        yield files
    finally:
        # Close all the files when done.
        for file in files.values():
            file.close()


# Store API key in a constant (better yet, fetch from environment variable or a secrets manager)
API_KEY = "pdf_live_3SxUghOiq0V2rWYUrBJuk6UPRCCCW8Tfjy4Yr7pLylu"  

# Example of how you'd call it:
folder_path = input("Please enter the folder path: ")
build_request_payload(folder_path)