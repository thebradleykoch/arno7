import os
import pyperclip
import assemblyai as aai
from datetime import datetime
from dotenv import load_dotenv


# Choose one of the following audio files to transcribe (uncomment one option below):
# Option 1: Local audio file
audio_file = "/Users/bradleykoch/Documents/Coding/Projects/arno7/audio_files/Laney Content Call 05 (Zoom Audio) (Voice Note AI).m4a"
# # Option 2: URL audio file (like Google Drive)
# audio_file = "https://drive.google.com/uc?export=download&id=12sf2SNmhaMV7IeRROFTezXO7lreWBfr8"


# Set the number of speakers expected in the audio file
speakers_expected = 3
# Define the speakers' names
speaker_a = "Laney"
speaker_b = "Jody"  # Add this when there's a second speaker
speaker_c = "Bradley"  # Add this when there's a third speaker


# Load environment variables from .env file
load_dotenv()

# Set API key from .env file
aai.settings.api_key = os.getenv('ASSEMBLY_AI_API_KEY')

# Set the transcription config (including custom vocabulary)
config = aai.TranscriptionConfig(
    speaker_labels=True,
    speakers_expected=speakers_expected,
    word_boost=[
        "Lara", "Nori", "Laney", "Bradley", "Aussie Doodle", "Dan Koe", "Matt Giaro",
        "Dickie Bush", "Nicolas Cole", "Justin Welsh", "Tim Denning", "Ramit Sethi", "Ali Abdaal",
        "Carter Surach", "Productive Dude", "Drake Surach", "AI Foundations", "Customer Desire Map",
        "ghostwriting", "Premium Ghostwriting Academy", "PGA", "Educational Email Course", "EEC",
        "Write With AI", "WWAI", "Typeshare", "Modern Mastery", "OpenAI", "OpenAI API Key", "Custom GPT", "ChatGPT",
        "Claude", "Sonnet", "Opus", "Arno",
        "TextCortex", "Map Of Content", "Rhetorical Structure",
        "Style Guide", "Rhythm Blocks", "Notion", "Obsidian", "Capacities", "Snipd", "SalesStory",
        "MusixMatch", "MaxQDA", "Terminix", "Vantage", "JavaScript",
        "HTML", "CSS", "Style Sheet", "Markdown", "Subject Line", "Lead", "CTA",
        "vs", "braindump", "gameplan"
    ],
    boost_param="high",
    disfluencies=False
    # audio_start_from=0,  # The start time of the transcription in milliseconds
    # audio_end_at=80000  # The end time of the transcription in milliseconds
)

# Create the transcriber object
transcriber = aai.Transcriber()

# Transcribe the audio file
transcript = transcriber.transcribe(
    audio_file,
    config=config
)


def format_timestamp(timestamp):  # Reformat the timestamps
    # Convert milliseconds to seconds
    seconds = timestamp / 1000
    # Format as [HH:MM:SS]
    return "[{:02d}:{:02d}:{:02d}]".format(int(seconds // 3600), int((seconds % 3600) // 60), int(seconds % 60))


# Transcribe the audio file
transcript = transcriber.transcribe(
    audio_file,
    config=config
)


# Map the speaker labels to their real names
if speakers_expected == 1:
    speaker_mapping = {"A": f"{speaker_a}"}
elif speakers_expected == 2:
    speaker_mapping = {"A": f"{speaker_a}", "B": f"{speaker_b}"}
elif speakers_expected == 3:
    speaker_mapping = {"A": f"{speaker_a}",
                       "B": f"{speaker_b}", "C": f"{speaker_c}"}

# Initialize an empty string to store the raw transcript
raw_transcript = ""

# # (Uncomment this section if there's only one speaker) Get the paragraphs and format them
# paragraphs = transcript.get_paragraphs()
# for paragraph in paragraphs:
#     start_time = format_timestamp(paragraph.start)
#     # Replace the speaker label with their actual name
#     speaker_name = speaker_a
#     raw_transcript += f"{start_time}\n**{speaker_name}:**\n{paragraph.text}\n\n"

# (Uncomment this line if there are multiple speakers) Print the transcript with correctly formatted timestamps and speaker labels
for utterance in transcript.utterances:
    start_time = format_timestamp(utterance.start)
    # Replace the speaker labels with their actual names
    speaker_name = speaker_mapping.get(utterance.speaker, utterance.speaker)
    raw_transcript += f"{start_time}\n**{speaker_name}:**\n{utterance.text}\n\n"

# Print and copy the transcript to the clipboard
print(raw_transcript)
pyperclip.copy(raw_transcript)

# Extract the base name of the original audio file without the extension
base_filename = os.path.splitext(os.path.basename(audio_file))[0]

# After generating the transcript, save it as a file
output_directory = "/Users/bradleykoch/Documents/Coding/Projects/arno7/transcripts/raw"
os.makedirs(output_directory, exist_ok=True)
output_filename = f"{base_filename} (Raw Transcript).md"
output_path = os.path.join(output_directory, output_filename)

with open(output_path, "w") as f:
    f.write(raw_transcript)

# Get the absolute path and format it as a clickable link
abs_path = os.path.abspath(output_path)
clickable_link = f"\033]8;;file://{abs_path}\033\\{abs_path}\033]8;;\033\\"

# Print completion message with timestamp
completion_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(
    f"Transcript generated and copied to clipboard. Saved to: {clickable_link}. Completed at {completion_time}.")
