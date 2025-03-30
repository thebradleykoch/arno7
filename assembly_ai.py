import os
import pyperclip
import assemblyai as aai
from datetime import datetime
from dotenv import load_dotenv


# Choose one of the following audio files to transcribe (uncomment one option below):
# Option 1: Local audio file
audio_file = "/Users/bradleykoch/Desktop/B-RAD/Summer Sales/The Grit/Sales Recordings/Mentor Recordings/Alec Sale – Stan (RACs on RACs).m4a"

# # Option 2: URL audio file (like Google Drive)
# audio_file = "https://drive.google.com/uc?export=download&id=12sf2SNmhaMV7IeRROFTezXO7lreWBfr8"


# Set the number of speakers expected in the audio file (1-10)
speakers_expected = 4

# Define speaker names - add as many as needed up to 10
# Leave empty strings for speakers that aren't present
speaker_names = [ 
                 # Make sure to add / remove commas after each speaker name in this list whenever you add or take speakers away... Otherwise, your speakers' names will come out merged like Siamese twins
    "Alec",
    "Wife",
    "Kid",
    "Stan",
    # "Speaker 5",
    # "Speaker 6",
    # "Speaker 7",
    # "Speaker 8",
    # "Speaker 9",
    # "Speaker 10"
]

# Choose which Custom Vocab List to use for this particular transcript
custom_vocab_list_voice_note = [
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
]
custom_vocab_list_salesstory = [
    "Terminix", "Greenix", "Moxie", "Fox", "Hawx", "Aptive", "All Star", "Patton",
    "Betts", "Best Pest", "Bug Stoppers", "Hassman", "TruGreen", "Champion Pest", "First Response"
    "local bug guy", "Do-It-Yourselfer", "DIYer", "initial", "initial service" "quarterly", "bimonthly", "reservice",
    "retreatment", "super cheap group rate", "group rate", "wasps", "wasps' nest", "mud daubers", "paper wasps", "ground hornets", "wolf spiders", "centipedes",
    "brown recluse", "pharaoh ants", "field mice", "carpenter bees",
    "silverfish", "fleas", "ticks", "voles", "house crickets", "field crickets",
    "ovipositor", "adult bugs", "eggs", "pupae", "larvae", "hatchlings", "pest control", "eco-friendly", "pheromones", "pheromone eraser", "Q-tip", "de-web", "eaves", "giant pole", "web-out", "granulation", "granulate", "granular", "granule",
    "fertilizer pellets", "premium liquid barrier", "power seal", "tick barrier",
    "bait boxes", "Ortho Home Defense", "Home Defense", "Spectracide", "Bifenthrin",
    "Terro Baits", "Borax", "1-year", "A-Frame", "Bradley Koch", "Mason Koch", "Alec Withers", "Jeremy Leavitt",
    "Matt Barrott", "Grayson Elwood", "Andrew Moffat", "Jacob Moffat", "Terminix", "Greenix"
]

# Load environment variables from .env file
load_dotenv()

# Set API key from .env file
aai.settings.api_key = os.getenv('ASSEMBLY_AI_API_KEY')

# Set the transcription config (including custom vocabulary)
config = aai.TranscriptionConfig(
    speech_model="best",
    speaker_labels=True,
    speakers_expected=speakers_expected,
    word_boost=custom_vocab_list_salesstory,  # Set to the correct Custom Vocab List
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


# Create speaker mapping dynamically
speaker_mapping = {}
for i in range(min(10, speakers_expected)):
    # Map letters A-J to speaker names, defaulting to "Speaker X" if name is empty
    speaker_letter = chr(65 + i)  # A, B, C, etc. up to J for 10 speakers
    speaker_name = speaker_names[i] if i < len(
        speaker_names) and speaker_names[i] else f"Speaker {i+1}"
    speaker_mapping[speaker_letter] = speaker_name

# Initialize an empty string to store the raw transcript
raw_transcript = ""

# Handle the formatting based on how many speakers there are
if speakers_expected == 1:
    paragraphs = transcript.get_paragraphs()
    for paragraph in paragraphs:
        start_time = format_timestamp(paragraph.start)
        raw_transcript += f"{start_time}\n**{speaker_names[0] or 'Speaker 1'}:**\n{paragraph.text}\n\n"
else:
    for utterance in transcript.utterances:
        start_time = format_timestamp(utterance.start)
        speaker_label = utterance.speaker
        speaker_name = speaker_mapping.get(
            speaker_label, f"Unknown Speaker ({speaker_label})")
        raw_transcript += f"{start_time}\n**{speaker_name}:**\n{utterance.text}\n\n"

# Print and copy the transcript to the clipboard
print(raw_transcript)
pyperclip.copy(raw_transcript)

# Extract the base name of the original audio file without the extension
base_filename = os.path.splitext(os.path.basename(audio_file))[0]

# After generating the transcript, save it as a file
output_directory = "/Users/bradleykoch/Documents/Coding/Projects/arno7/transcripts/raw"
os.makedirs(output_directory, exist_ok=True)
output_filename = f"{base_filename} (Voice Note AI) (Raw Transcript).md"
output_path = os.path.join(output_directory, output_filename)

# Create the header by removing the extension using os.path.splitext()
header = f"# {os.path.splitext(output_filename)[0]}\n\n"

# Combine the header with the transcript content
final_content = header + raw_transcript

with open(output_path, "w") as f:
    f.write(final_content)

# Get the absolute path and format it as a clickable link
abs_path = os.path.abspath(output_path)
clickable_link = f"\033]8;;file://{abs_path}\033\\{abs_path}\033]8;;\033\\"

# Print completion message with timestamp
completion_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(
    f"Transcript successfully generated and copied to clipboard. Saved to: {clickable_link}. Completed at {completion_time}.")
