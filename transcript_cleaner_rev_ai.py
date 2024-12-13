# A Script To Clean My Rev AI Voice Notes & Summer Sales Recording Transcripts

import re
import os
import html
import urllib.parse

# Specify the input and output folders at the beginning for easy modification
input_folder = '/Users/bradleykoch/Downloads/Laney Content Call'
output_folder = '/Users/bradleykoch/Downloads/Laney Content Call'

speaker_0 = "Bradley"
speaker_1 = "Laney"
speaker_3 = "Speaker 3"
speaker_4 = "Speaker 4"

# Define a dictionary to map written numbers to digit forms
number_map = {
    "two": "2", "three": "3", "four": "4", "five": "5",
    "six": "6", "seven": "7", "eight": "8", "nine": "9",
    "ten": "10", "eleven": "11", "twelve": "12",
    "thirteen": "13", "fourteen": "14", "fifteen": "15",
    "sixteen": "16", "seventeen": "17", "eighteen": "18",
    "nineteen": "19", "twenty": "20"
}

# Function to replace written numbers with digit forms


def replace_numbers(match):
    return number_map[match.group(0)]


# Compile the pattern for number replacement
number_pattern = re.compile(r'\b(' + '|'.join(number_map.keys()) + r')\b')


def clean_transcript_content(content):
    # This function cleans the transcripts using Regex
    cleaned_content = content  # Initialize cleaned_content with the input content

    # Replace speaker labels with actual names
    cleaned_content = re.sub(r'Speaker\s+0\s+(\d\d:\d\d:\d\d)\s+(.+)',
                             r'[\1]\n{}:\n\2\n\n'.format(speaker_0), cleaned_content)
    cleaned_content = re.sub(r'Speaker\s+1\s+(\d\d:\d\d:\d\d)\s+(.+)',
                             r'[\1]\n{}:\n\2\n\n'.format(speaker_1), cleaned_content)
    cleaned_content = re.sub(r'Speaker\s+3\s+(\d\d:\d\d:\d\d)\s+(.+)',
                             r'[\1]\n{}:\n\2\n\n'.format(speaker_3), cleaned_content)
    cleaned_content = re.sub(r'Speaker\s+4\s+(\d\d:\d\d:\d\d)\s+(.+)',
                             r'[\1]\n{}:\n\2\n\n'.format(speaker_4), cleaned_content)

    # Clean up context tags <>
    cleaned_content = re.sub(r'>(,|\s)', r'>. ', cleaned_content)

    # Get rid of context tags <>
    cleaned_content = re.sub(r'\s*<.+?>.', r'', cleaned_content)

    # Capitalize the first letter of the first word after a newline
    cleaned_content = re.sub(r'(:\s*\n[a-z])|(\n+[a-z])', lambda x:  x.group(
        0).upper() if x.group(0).islower() else x.group(0).lower(), cleaned_content)

    # Capitalize the first letter of the first word after a period or question mark
    cleaned_content = re.sub(r'(\.|\?)\s+\'?[a-z]', lambda y: y.group(0).upper() if y.group(
        0).islower() else y.group(0).lower(), cleaned_content, flags=re.M | re.X)

    # # Remove duplicate words
    # cleaned_content = re.sub(
    #     r'\b([A-Za-z]+(\'?[A-Za-z]+)?)([ \t]+|,)[ \t]*\1(\b)', r'\1', cleaned_content)

    # # Attribute affirmative context tags to correct speakers
    # cleaned_content = re.sub(
    #     r'(?<!\n)(Mm-hmm\.\s<affirmative>(\.|,)*\s*|Mm-hmm(\.|,)*\s*)', r'\n\n\n\1\n\n\n', cleaned_content)

    # # Fix pricing numbers
    # cleaned_content = re.sub(
    #     r'(\d+)([ \t]+|[^\n,.:\d])(\d+)', r'\1\3', cleaned_content)

    # # Replace 'cuz' with 'cause
    # cleaned_content = re.sub(r"(?<!be)(cuz|cause)", r"'cause", cleaned_content)

    # # Remove duplicate spaces between words
    # cleaned_content = re.sub(r'([A-Za-z])\s{2,}(.)', r'\1 \2', cleaned_content)

    # # Attach dangling statements to next speaker
    # cleaned_content = re.sub(
    #     r'-(\s*\n+.+\n.+\s*\n)(([A-Za-z]+.)\B\s*)', r' \3\1', cleaned_content)

    # # Attach dangling statements to next speaker
    # cleaned_content = re.sub(
    #     r'([A-Z]+[a-z]*\'?[ \t]?[A-Za-z]*,?[ \t]?[A-Za-z]+[ \t]?[A-Z]*[a-z]*\'?[ \t]?)(\n|[^\n:-])\n+(\d\d:\d\d:\d\d\s*\n.+\n)([A-Za-z]+\'?[ \t]?([a-z]+.[ \t]?)?)', r'\n\n\n\3\1\4', cleaned_content)

    # # Fix commas and periods with no space afterwards
    # cleaned_content = re.sub(
    #     r'([A-Za-z])(,|\.)([A-Za-z])', r'\1\2 \3', cleaned_content)

    # # Fix newline spacing
    # cleaned_content = re.sub(
    #     r'(.)\n{1,2}(\d\d:)', r'\1\n\n\n\2', cleaned_content)

    # # Add newline after Speaker Label if dialogue is stuck on same line
    # cleaned_content = re.sub(
    #     r'(:\d\d\n[A-Za-z]+:)([A-Za-z])', r'\1\n\2', cleaned_content)

    # # Fix out-of-place timestamps
    # cleaned_content = re.sub(r'.(\d\d:\d\d:\d\d)',
    #                          r'\n\n\n\1', cleaned_content)

    # # Eliminate speaker labels with no dialogue
    # cleaned_content = re.sub(
    #     r'\d\d:\d\d:\d\d\n[A-Za-z]+:\n\s+', r'', cleaned_content)

    # # Reattach <affirmative> tags to Mm-hmm text
    # cleaned_content = re.sub(
    #     r'(Mm-hmm\.\s?)(\s*\n+)(\d\d:\d\d:\d\d\n.+)\n(\s?<affirmative>\.\s?)', r'\1\4\n\n\n\3\n', cleaned_content)

    # Remove filler words
    cleaned_content = re.sub(
        r'(([^A-Za-z])(Uh,*[^-]\s*))|(([^A-Za-z])(Um,*\s*))', r'\2\5', cleaned_content)

    # Convert written-out numbers to math / integer-style numbers
    cleaned_content = number_pattern.sub(replace_numbers, cleaned_content)

    # Fix any HTML entity substitutions
    cleaned_content = html.unescape(cleaned_content)

    return cleaned_content


def process_single_file(filepath, output_folder):
    # This function processes a single file
    with open(filepath, 'r', encoding='utf-8') as file:
        original_content = file.read()

    # Clean the content
    cleaned_content = clean_transcript_content(original_content)

    # Construct the new file path in the output directory
    filename = os.path.basename(filepath)
    new_filepath = os.path.join(output_folder, filename)

    # Write the cleaned content to a new file
    with open(new_filepath, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)

    # Create and print a clickable link in VS Code terminal
    url_encoded_path = urllib.parse.quote(new_filepath)
    clickable_url = f"file://{url_encoded_path}"
    print(f"Cleaned content written to: {clickable_url}")


def batch_process_folder(input_folder, output_folder):
    # This function batch processes all Markdown and plain text files in the input directory
    for filename in os.listdir(input_folder):
        if filename.endswith((".md", ".txt")):  # Checks if the file is a Markdown or plain text file
            filepath = os.path.join(input_folder, filename)
            process_single_file(filepath, output_folder)


    # Create and print a clickable link in VS Code terminal
    url_encoded_path = urllib.parse.quote(output_folder)
    clickable_url = f"file://{url_encoded_path}"
    print(f"Cleaned content written to: {clickable_url}")

# Main function to run


def main():
    # For batch processing, call batch_process_folder
    # For single file processing, call process_single_file with the specific file path

    # Uncomment one line or the other below (choose between batch processing & single-file processing)

    batch_process_folder(input_folder, output_folder)
    # process_single_file(input_folder, output_folder)


if __name__ == "__main__":
    # This function ensures the code is only executed if it's run directly (so this script won't run if it's just being imported by another module)
    main()
