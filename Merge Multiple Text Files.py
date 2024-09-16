# Merge Multiple Text Files
## Format spacing and text hierarchy, logically split text blocks into paragraphs 


import os

def merge_txt_files(input_files, output_file):
    # Initialize the merged text as an empty string
    merged_text = ""

    # Iterate over each input file
    for file in input_files:
        with open(file, 'r') as f:
            # Read the contents of the file
            file_contents = f.read()

            # Append the contents to the merged text with three blank lines between files
            merged_text += file_contents + '\n\n\n'

    # Split the merged text into paragraphs based on logical subject changes
    paragraphs = split_into_paragraphs(merged_text)

    # Write the merged and formatted text to the output file
    with open(output_file, 'w') as f:
        # Write the file name at the beginning without the extension
        file_name = os.path.splitext(os.path.basename(output_file))[0]
        f.write('# ' + file_name + '\n\n\n')

        # Write each paragraph to the file with an empty line between paragraphs
        for paragraph in paragraphs:
            f.write(paragraph + '\n\n')

def split_into_paragraphs(text):
    # Split the text into individual lines
    lines = text.splitlines()

    # Initialize the paragraphs list with the first line as the first paragraph
    paragraphs = [lines[0]]

    # Iterate over the remaining lines
    for line in lines[1:]:
        # Check if the line is empty or starts with a title
        if not line.strip() or line.strip().startswith('#'):
            # Add a new paragraph with the line
            paragraphs.append(line)
        else:
            # Add the line to the current paragraph
            paragraphs[-1] += ' ' + line

    return paragraphs
