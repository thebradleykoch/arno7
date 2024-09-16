import os
import time
import pyperclip
from datetime import datetime
from dotenv import load_dotenv
from anthropic import Anthropic, APIError

# Load environment variables and set API key
load_dotenv()
api_key = os.getenv('ANTHROPIC_API_KEY')

# Initialize Anthropic client
client = Anthropic()

# Set model and headers
ai_model = "claude-3-5-sonnet-20240620"
extra_headers = {"anthropic-beta": "max-tokens-3-5-sonnet-2024-07-15"}


def chunk_generator(transcript, chunk_size=8000):
    words = transcript.split()
    current_chunk = []
    current_size = 0
    for word in words:
        if current_size + len(word) > chunk_size:
            yield " ".join(current_chunk)
            current_chunk = [word]
            current_size = len(word)
        else:
            current_chunk.append(word)
            current_size += len(word) + 1
    if current_chunk:
        yield " ".join(current_chunk)


def load_latest_transcript():
    raw_transcript_dir = "/Users/bradleykoch/Coding/Projects/arno7/transcripts/raw"
    latest_transcript = max([os.path.join(raw_transcript_dir, f)
                            for f in os.listdir(raw_transcript_dir)], key=os.path.getmtime)

    with open(latest_transcript, "r") as f:
        return f.read(), latest_transcript


def process_transcript(raw_transcript):
    chunks = list(chunk_generator(raw_transcript))
    total_chunks = len(chunks)
    cleaned_transcript = ""

    system_prompt = """
    # Voice Note Transcript Reformatting Instructions (V4-Shot)

    Hey Arno, I need your help reformatting & cleaning up my Voice Note Transcript. Here's the gameplan:
    
    1. I'll pass you parts of the raw transcript.
    2. You'll follow the reformatting instructions for each part.
    3. Continue from where you left off in the previous part.

    We'll go one step at a time. You tracking with me?

    ## Part 1: Content & Vocabulary

    **Clean up and reformat the transcript by following these 2 steps:**

    1. **Preserve Original Content**
        - DON'T SUMMARIZE or cut out the transcript's original content.
        - Keep your transcript output as close to the original input as possible — *almost exactly* word for word.
        - Preserve the speaker's original words and sentences, including personal voice & style (slang, etc.). DON'T substitute in formal words & phrases for casual & conversational ones.

    2. **Apply Custom Vocabulary**
        Fix any misspelled terms in the transcript that match the correctly spelled versions in this list:
        - Lara
        - Laney
        - Bradley
        - Aussie Doodle
        - Fine & Dandy
        - Dan Koe
        - Matt Giaro
        - Dickie Bush
        - Nicolas Cole
        - Justin Welsh
        - Tim Denning
        - Ramit Sethi
        - Ali Abdaal
        - Carter Surach
        - Productive Dude
        - Drake Surach
        - AI Foundations
        - Customer Desire Map
        - Premium Ghostwriting Academy
        - PGA
        - Educational Email Course
        - EEC
        - 5-Day Educational Email Course
        - 5-Day EEC
        - Ship 30 For 30
        - Write With AI
        - Typeshare
        - 2 Hour Writer
        - Modern Mastery
        - OpenAI
        - OpenAI API Key
        - Custom GPT
        - ChatGPT-4o
        - ChatGPT
        - GPT-4o
        - Claude 3.5 Sonnet
        - Claude 3 Opus
        - Claude
        - Sonnet
        - Opus
        - Arno
        - Arno7
        - TextCortex
        - Map Of Content
        - Rhetorical Structure
        - Rhetorical + Elemental Structure
        - Style Guide
        - Rhythm Blocks
        - Notion
        - Obsidian
        - Capacities
        - Snipd
        - SalesStory
        - MusixMatch
        - MaxQDA
        - Atlas.ti
        - Terminix
        - Vantage
        - H1, H2, H3
        - JavaScript
        - HTML
        - CSS
        - Style Sheet
        - Markdown
        - Markdown-formatted
        - Subject Line
        - Lead
        - CTA
        - vs
        - braindump

    **Remember:** DON'T summarize or consolidate the transcript's original content.

    ## Part 2: Structure & Formatting

    **Make these structure and formatting changes:**

    1. Insert paragraph breaks / newlines every 2-4 sentences. Cap massive run-on sentences with a period, especially when breaking up paragraphs.

    2. Clean up awkwardly placed commas or wonky punctuation (maintain thinking-out-loud phrases, but aim for easy-to-read content).

    3. Replace words like "slash" with their associated character "/".

    4. Replace ALL written-out numbers with math-style numbers ("four" → "4", "fourth" → "4th", "number two" → "number 2", etc.) — except for sentences where it makes more sense to say "one" instead of "1".

    5. Add a space before and after forward slashes "/" and em-dashes "—" (except in URLs or links).

    6. Don't use semicolons ";" to punctuate content (except if absolutely necessary, like in coding syntax).

    7. Replace "<laugh>" with "Haha." Remove other XML-like tags with their accompanying terms like, "Mmhmm <affirmative>", "Uhhuh <affirmative>", etc. (but KEEP timestamps "[00:01:23]"). Also, remove filler words like "Um" or "Uh". Correct the punctuation around these removals for natural flow.

    8. If there's more than one speaker, follow these exact steps below when formatting the timestamps, speaker labels, and dialogue content:
        - Always maintain 2 newlines before timestamps.
        - Always maintain 1 newline after timestamps, speaker labels, and dialogue content.
        - Ensure consistent spacing throughout the transcript.
        - Do not add extra spaces or newlines beyond what's specified here.
        - Example Format:
            ```markdown
            [Previous content ends here]

            [00:00:22]
            **Speaker Name:**
            Dialogue content goes here...

            [00:00:33]
            **Speaker Name:**
            Dialogue content goes here...

            [Next timestamp starts here]
            ```

    9. Add descriptive subheads (H2s) throughout the transcript to create structure (like sections or chapters), so I can easily navigate the main ideas visually and logically.

    10. Identify and properly format hypothetical dialogue. When the speaker is mimicking or describing a conversation (often starting with phrases like "I'll say" or "I tell it" or "Like"), enclose this dialogue in quotation marks to distinguish it from the speaker's main narrative.

    11. Smooth out speech disfluencies:
        - Remove excessive repetitions of words or phrases, keeping only one instance unless the repetition serves a purpose (like emphasis).
        - Clean up false starts by removing the incomplete phrase if it doesn't add meaning.
        - Keep some filler words like "like" and "you know" to maintain the conversational tone, but remove them if they appear too frequently or disrupt the flow.
        - Remove excessive hesitations like "um" and "uh."
        - For revisions, choose the clearer or more complete version of the statement. We wanna smooth out disfluencies for readability, without changing the core content or conversational style of the speakers.
        - Example:
            - Original: "It's, it, it spills over when the moms take care of the kids. It really does. It spills over."
            - Smoothed: "It spills over when the moms take care of the kids. It really does spill over."

    12. Skip the preamble and go straight to the content. No post-amble either.
    
    **Output Format:** When reformatting the transcript, output your response in markdown format (rendered as rich text) following the instructions from both Part 1 and Part 2.

    If the transcript is long and you need to reformat it in chunks over the course of several responses, then just continue your next message from where you left off in your previous response. Once you've finished processing the entire transcript (all chunks), lemme know by saying "TRANSCRIPT_COMPLETE".
    
    Go ahead and start reformatting the transcript now.
    """

    conversation_history = []

    for i, chunk in enumerate(chunks, 1):
        print(f"Processing chunk {i}/{total_chunks}")

        try:
            messages = [{"role": "user", "content": f"""
                         Process this part of the transcript:
                         
                         {chunk}"""}]
            if conversation_history:
                messages.extend(conversation_history)

            response = client.messages.create(
                model=ai_model,
                max_tokens=8192,
                temperature=0.5,
                system=system_prompt,
                extra_headers=extra_headers,
                messages=messages
            )

            if response.content and isinstance(response.content, list) and len(response.content) > 0:
                chunk_output = response.content[0].text
                cleaned_transcript += chunk_output
                print(
                    f"Chunk {i} processed. Output length: {len(chunk_output)}")
                print("Preview of processed chunk:")
                print(
                    chunk_output[:500] + "..." if len(chunk_output) > 500 else chunk_output)

                if "TRANSCRIPT_COMPLETE" in chunk_output:
                    print("AI signaled transcript completion.")
                    cleaned_transcript = cleaned_transcript.replace(
                        "TRANSCRIPT_COMPLETE", "").strip()
                    break

                conversation_history = [
                    {"role": "assistant", "content": chunk_output}]
            else:
                print(
                    f"Unexpected response format for chunk {i}. Skipping this chunk.")

        except APIError as e:
            print(f"API error occurred: {e}")
            print(f"Skipping chunk {i} due to error.")
        except Exception as e:
            print(f"Unexpected error occurred while processing chunk {i}: {e}")
            print(f"Skipping chunk {i} due to error.")

        if i == total_chunks:
            print("Reached the last chunk.")

    print(f"Total processed transcript length: {len(cleaned_transcript)}")
    return cleaned_transcript


def save_cleaned_transcript(cleaned_transcript, original_filename):
    output_directory = "/Users/bradleykoch/Coding/Projects/arno7/transcripts/cleaned"
    os.makedirs(output_directory, exist_ok=True)

    base_filename = os.path.basename(original_filename)
    output_filename = base_filename.replace(
        "Raw Transcript", "Cleaned Transcript")
    if not output_filename.endswith('.md'):
        output_filename += '.md'
    output_path = os.path.join(output_directory, output_filename)

    with open(output_path, "w") as f:
        f.write(cleaned_transcript)

    return output_path


def save_cleaned_transcript(cleaned_transcript, original_filename):
    output_directory = "/Users/bradleykoch/Coding/Projects/arno7/transcripts/cleaned"
    os.makedirs(output_directory, exist_ok=True)

    base_filename = os.path.basename(original_filename)
    output_filename = base_filename.replace(
        "Raw Transcript", "Cleaned Transcript")
    if not output_filename.endswith('.md'):
        output_filename += '.md'
    output_path = os.path.join(output_directory, output_filename)

    with open(output_path, "w") as f:
        f.write(cleaned_transcript)

    return output_path


def main():
    raw_transcript, original_filename = load_latest_transcript()
    cleaned_transcript = process_transcript(raw_transcript)

    # Print and copy the cleaned transcript to the clipboard
    print(cleaned_transcript)
    pyperclip.copy(cleaned_transcript)

    # Save the cleaned transcript
    output_path = save_cleaned_transcript(
        cleaned_transcript, original_filename)

    # Get the absolute path and format it as a clickable link
    abs_path = os.path.abspath(output_path)
    clickable_link = f"\033]8;;file://{abs_path}\033\\{abs_path}\033]8;;\033\\"

    # Print the completion message
    completion_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(
        f"Transcript cleaned and copied to clipboard. Saved to: {clickable_link}. Completed at {completion_time}.")


if __name__ == "__main__":
    main()
