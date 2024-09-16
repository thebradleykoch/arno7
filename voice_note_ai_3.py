import os
import pyperclip
from datetime import datetime
from dotenv import load_dotenv
from anthropic import Anthropic
from custom_instructions import system_prompt

# Load environment variables and set API key
load_dotenv()
api_key = os.getenv('ANTHROPIC_API_KEY')

# Initialize Anthropic client
client = Anthropic()

# Set model and headers
ai_model = "claude-3-5-sonnet-20240620"
extra_headers = {"anthropic-beta": "max-tokens-3-5-sonnet-2024-07-15"}


def load_latest_transcript():
    raw_transcript = ""
    raw_transcript_dir = "/Users/bradleykoch/Coding/venvs/envspot/bin/transcripts/raw"
    latest_transcript = max([os.path.join(raw_transcript_dir, f)
                            for f in os.listdir(raw_transcript_dir)], key=os.path.getmtime)

    with open(latest_transcript, "r") as f:
        raw_transcript = f.read()
        return raw_transcript, latest_transcript


response = client.messages.create(
            model=ai_model,
            max_tokens=8192,
            temperature=0.5,

message=client.messages.create(
    model=ai_model,
    max_tokens=8192,
    temperature=0.5,
    system=system_prompt,
    extra_headers=extra_headers,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": """
                    # Voice Note Transcript Reformatting Instructions (V4-Shot)

                    Hey Arno, I need your help reformatting & cleaning up my Voice Note Transcript.

                    Here's the gameplan:

                    1. In a moment, I'll pass you the raw transcript. Just say "Got it" when you receive the content.
                    2. Then, I'll pass you the reformatting instructions (which are split into 2 parts).
                    3. You'll follow part 1 of the instructions first, then part 2.

                    We'll go one step at a time. You tracking with me?
                    """
                }
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": "Yeah man, I'm with you. Sounds like a solid plan. Hit me with that raw transcript whenever you're ready, and I'll give you the \"Got it\" signal. Then we'll tackle those reformatting instructions one by one. Let's do this."
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"""
                    Here's the transcript...

                    (remember to confirm first, then wait for the "part 1 instructions")

                    <raw_transcript>

                    {raw_transcript}

                    </raw_transcript>
                    """
                }
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": "Got it"
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": """
                    # Voice Note Transcript Reformatting Instructions – Part 1/2

                    Aight, here's part 1:

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
                        - Kortex
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
                        - Step 1: Self-Prompt (Topic & Idea Generation)
                        - Step 2: Braindump (Unique Perspective)
                        - Step 3: Outline (Main Points & Subpoints)
                        - Step 4: First Draft (Structure & Style)
                        - Step 5: Final Draft (Edit & Publish
                        - braindump or braindumping (INSTEAD OF "brain dump", "brain-dump", "brain dumping", or "brain-dumping")
                        - vs (INSTEAD OF "versus", "Vs", "Vs.", or "vs.")

                    **Remember:** DON'T summarize or consolidate the transcript's original content.

                    Once you've studied Part 1 (Content & Vocabulary), let's move on to Part 2 (Structure & Formatting).

                    Ready?
                    """
                }
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": "Alright, I've got Part 1 down. I'll make sure to preserve the original content, keep it word-for-word as much as possible, and apply the custom vocabulary list. I won't summarize or cut anything out, and I'll maintain the speakers' original style and casual language. Hit me with Part 2 whenever you're ready."
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": """
                    # Voice Note Transcript Reformatting Instructions – Part 2/2

                    Sweet, now let's move on to part 2:

                    ## Part 2: Structure & Formatting

                    **Make these structure and formatting changes:**

                    1. Insert paragraph breaks / newlines every 2-4 sentences. Cap massive run-on sentences with a period, especially when breaking up paragraphs.

                    2. Clean up awkwardly placed commas or wonky punctuation (maintain thinking-out-loud phrases, but aim for easy-to-read content).

                    3. Replace words like "slash" with their associated character "/".

                    4. Replace written-out numbers with math-style numbers ("four" → "4", "fourth" → "4th", "number two" → "number 2", etc.) — EXCEPT for when using the word "one" instead of the number "1" makes more sense and looks more natural in the context of the text.

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

                    9. Add descriptive subheads (H2s) throughout the transcript to create structure and coherence (like sections or chapters), so I can easily navigate the main ideas visually and logically.

                    10. Identify and properly format hypothetical dialogue. When the speaker is mimicking or describing a conversation (often starting with phrases like "I'll say" or "I tell it" or "Like"), enclose this dialogue in quotation marks to distinguish it from the speaker's main narrative.

                    11. Smooth out speech disfluencies:
                        - Clean up false starts and stutters by removing excessive repetitions of words or phrases (like stammers) if they don't add meaning.
                        - Keep some natural filler words like "like" and "you know" to maintain the conversational tone, but remove them if they appear too frequently or disrupt the flow.
                        - Remove excessive filler words or hesitations like "um" and "uh".
                        - Smooth out disfluencies and choppy sentences for readability, without changing the core content or conversational style of the speakers.
                        - Example:
                            - Original: "It's, it, it spills over when the moms take care of the kids. It really does. It spills over."
                            - Smoothed: "It spills over when the moms take care of the kids. It really does spill over."

                    12. When you output your response, skip the preamble and just go straight to the content. (Ditch the post-amble too.)

                    **Output Format:** When reformatting the transcript, output your response in markdown format (rendered as rich text) following the instructions from both Part 1 and Part 2.

                    Go ahead and execute these complete instructions now (on the raw transcript I gave you earlier).
                    """
                }
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": """

							# [assistant's response appears here]...

							"""
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": """
							Continue... (If you haven't finished reformatting the entire transcript content yet, then keep modifying the same markdown-formatted rich text, picking back up where you left off. Once you've finished reformatting the ENTIRE transcript, lemme know by closing with this line at the very end:

							<!-- transcript complete -->
							"""
                }
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": """

							# [assistant's response appears here]...

							"""
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": """
							Continue... (If you haven't finished reformatting the entire transcript content yet, then keep modifying the same markdown-formatted rich text, picking back up where you left off. Once you've finished reformatting the ENTIRE transcript, lemme know by closing with this line at the very end:

							<!-- transcript complete -->
							"""
                }
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": """

							# [assistant's response appears here]...

							"""
                }
            ]
        }
    ]
)
print(message.content)
