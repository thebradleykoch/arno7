# Master Plan For My Voice Note AI System

## Relevant Files & Directories

- `voice_note_ai_anthropic.py`
- `assembly_ai.py`
- `custom_instructions.py`
- `transcripts/raw/`
- `transcripts/cleaned/`
- `transcripts/refined/`

## Workflow

1. `assembly_ai.py` transcribes the audio file and saves it to `transcripts/raw/`.
2. `voice_note_ai_anthropic.py` then cleans and reformats the transcript, saving it to `transcripts/cleaned/`.

## Next Steps

- [ ] Fix the timestamp format for the `/transcripts/cleaned/` output file path in `voice_note_ai_anthropic.py`.
- [ ] Add a "while" loop to `voice_note_ai_anthropic.py` to allow long transcripts to be processed in chunks.
- [ ] Add a "while" loop to `assembly_ai.py` to allow long audio files to be processed in chunks. (But first: Does Assembly AI have an audio file size / length limit, or can it handle any length?)
- [ ] Figure out how to output the cleaned transcript to a "Voice Notes" Notion database via the Notion API. (Use my "AssemblyAI Outputs" database.)
