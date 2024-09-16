# Voice Note AI Project Overview

## What I'm Trying to Achieve (Goal & Purpose)

I'm working on building a Python script that uses the Anthropic API to transcribe and reformat long audio files, like hour-long sales call transcripts. The main issue I'm running into is that these transcripts are too long for a single API call due to prompt-response cycle token limitations. So I'm looking to create a multi-turn conversation that can handle the entire transcript.

My goal is to have the AI reformat the transcript piece by piece, continuing where it left off each time it hits the token limit, until the entire transcript is processed. I wanna do this efficiently, without having to manually prompt it to continue each time.

## Obstacles I'm Facing (Challenges & Roadblocks)

1. How to structure the multi-turn conversation
2. How to tell the AI to continue where it left off and handle the "continue" logic without unnecessarily repeating messages
3. How to tell the AI to signal when it's done reformatting the entire transcript

## "Unknown Unknowns" to Consider (Barriers & Uncertainties)

1. How to structure my code to make it practical, effective, and efficient — so it can easily handle any length of transcript and any type of reformatting instructions
2. How to approach the thinking (the "what" and the "why") like a senior developer: choosing the best methods and solutions while anticipating potential issues and thinking through the logic clearly

## Success Criteria (My Ideal Outcome)

I want a script that can:

1. Take any length of transcript as an input
2. Process it effectively through multiple API calls (without manual intervention)
3. Automatically continue where it left off each time (in the correct place)
4. Stop when the entire transcript is completely processed
5. Output the fully reformatted transcript as a single, cohesive markdown file

   - Combine all reformatted transcript output responses into one document
   - Ensure each piece of the cleaned transcript connects seamlessly to the next (no gaps or formatting quirks)
   - Make it look like the entire original transcript was processed in one go, with no breaks or interruptions
   - Begin and end the transcript with only the actual content (no preamble or post-amble)
