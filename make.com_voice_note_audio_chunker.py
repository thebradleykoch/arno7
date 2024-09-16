# Split Audio Google Cloud Function

import functions_framework
from pydub import AudioSegment  # Importing PyDub to handle audio operations
import math  # Importing math to handle calculations for chunking
import os  # Importing os for file operations
# Importing Google Cloud Storage client to handle file storage
from google.cloud import storage


@functions_framework.http
def split_audio(request):
    # Step 1: Parse the incoming request
    request_json = request.get_json()  # Extract JSON data from the HTTP request
    # Get the file path from the JSON data
    file_path = request_json['file_path']
    # Default chunk length is 10 minutes (600,000 ms)
    chunk_length_ms = request_json.get('chunk_length_ms', 600000)
    # Default overlap is 1 second
    overlap_ms = request_json.get('overlap_ms', 1000)

    # Step 2: Initialize Google Cloud Storage client and download the audio file
    storage_client = storage.Client()  # Create a storage client
    bucket = storage_client.bucket(
        'make_input_audio')  # Using your bucket name
    blob = bucket.blob(file_path)  # Get the blob (file) from the bucket
    # Download the file to a temporary location with the same extension
    temp_audio_path = f'/tmp/temp_audio_file.{file_path.split(".")[-1]}'
    # Download the file to a temporary location
    blob.download_to_filename(temp_audio_path)

    # Step 3: Load the audio file using PyDub
    audio = AudioSegment.from_file(temp_audio_path)  # Load the audio file
    # Get the total length of the audio in milliseconds
    total_length = len(audio)

    # Step 4: Calculate the number of chunks needed
    # Calculate number of chunks
    num_chunks = math.ceil(total_length / (chunk_length_ms - overlap_ms))

    chunks = []  # List to store chunk file URLs

    # Step 5: Split the audio into chunks and upload each chunk
    for i in range(num_chunks):
        # Calculate start time for the chunk
        start = i * (chunk_length_ms - overlap_ms)
        end = start + chunk_length_ms  # Calculate end time for the chunk
        chunk = audio[start:end]  # Extract the chunk from the audio
        # Path to save the chunk locally with the same extension
        chunk_path = f"/tmp/chunk_{i}.{file_path.split('.')[-1]}"
        # Export the chunk with the same format
        chunk.export(chunk_path, format=file_path.split('.')[-1])

        # Upload the chunk to Google Cloud Storage
        # Create a new blob for the chunk
        chunk_blob = bucket.blob(
            f'chunks/chunk_{i}.{file_path.split(".")[-1]}')
        chunk_blob.upload_from_filename(chunk_path)  # Upload the chunk file
        # Add the public URL of the chunk to the list
        chunks.append(chunk_blob.public_url)

    # Step 6: Return the list of chunk URLs
    # Return the list of chunk URLs as a JSON response
    return {'chunks': chunks}


# @functions_framework.http
# def split_audio_get(request):
#     """HTTP Cloud Function.
#     Args:
#         request (flask.Request): The request object.
#         <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
#     Returns:
#         The response text, or any set of values that can be turned into a
#         Response object using `make_response`
#         <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
#     Note:
#         For more information on how Flask integrates with Cloud
#         Functions, see the `Writing HTTP functions` page.
#         <https://cloud.google.com/functions/docs/writing/http#http_frameworks>
#     """
#     return 'Split Audio!'
