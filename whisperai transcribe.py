# whisperai transcribe
import os
import openai
import whisper
import requests

# Set up the OpenAI API key
openai.api_key = "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"

# Define the local audio file to transcribe
audio_file = "/Users/bradleykoch/Library/Mobile Documents/com~apple~CloudDocs/SALES/Wyndham Sales Recordings/Recordings - Transcribe Next/Bradley Koch - 1k Kristen.m4a"

# Transcribe the audio file using WhisperAI
response = openai.Function.create(
    function="whisperai/transcribe-audio-file",
    inputs={
        "audio_file": {
            "url": "file://" + os.path.abspath(audio_file)
        }
    },
    outputs=["transcript"]
)

# Get the transcript
transcript = response["results"]["transcript"]

# Name the finished transcript file
transcript_file = "/Users/bradleykoch/Library/Mobile Documents/com~apple~CloudDocs/SALES/Wyndham Sales Recordings/Recordings - Transcribe Next/Bradley Koch - 1k Kristen WhisperAI Transcript.txt"

# Save the transcript as a text file
with open(transcript_file, "w") as f:
    f.write(transcript)
    print("Transcript saved successfully.")
