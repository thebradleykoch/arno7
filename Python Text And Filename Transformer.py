# Python Text Transformer: Reformat "Write With AI" PDF Filenames


import os
import shutil
import re  # Importing the regular expression module

# Function to transform the filename
def transform_filename(filename):
    # Replace all quotes with single quotes
    step1 = filename.replace('"', "'").replace("“", "'").replace("”", "'")
    
    # Extract the name and extension
    name, extension = os.path.splitext(step1)
    
    # If the filename starts with "Write With AI – ", keep it as is; otherwise, prepend it
    if name.startswith("Write With AI – "):
        step2 = f'"{name}"{extension}'
    else:
        step2 = f'Write With AI – "{name}"{extension}'
    
    # Replace underscores followed by spaces with " - "
    step3 = step2.replace("_ ", " - ")

    # Check for duplicate "Write With AI – "
    if re.search(r"Write With AI – ", step3):
      step4 = f'{step3}'  
    else:
      step4 = f'Write With AI – {step3}' 
    

    # Replace duplicate / unnecessary spaces
    step5 = re.sub(r'\s{2,}', ' ', step4)
    # Remove duplicate "Write With AI – " phrases
    step5 = re.sub(r'(Write With AI – ){2,}', r'\1', step5)
    # Replace duplicate / unnecessary quotation marks
    step5 = re.sub(r'\"+(Write With AI –)', r'\1', step5)  # Using \1 for backreference
    step5 = re.sub(r'\"{2,}', '"', step5)  # Replace multiple double quotes with a single one
    step5 = re.sub(r"\'{2,}", "'", step5)  # Replace multiple single quotes with a single one
        # Annihilate any single quotes 
    step5 = re.sub(r'(?<=\')((.*)(\")(.*))+(?=\'\.pdf)', r"\2'\4", step5)
    step5 = re.sub(r'(?<!\")((.*)(\')(.*))+(?!\"\.pdf)', r'\2"\4', step5)
    step5 = re.sub(r'(?<=Write With AI –\s)((.*)(\')(.*))+(?=\.pdf)', r'\2"\4', step5)
    step5 = re.sub(r"((?<=\")((.*)(\")))+(.+?)(?!\.pdf)", r"\3'\5", step5)
    step6 = re.sub(r'((?<!(\"|\'))(\"|\'))+', r'"', step5)
    step6 = re.sub(r'((\"|\')(?!(\"|\')))+', r'"', step6)
    step6 = re.sub(r'((?<=(\"|\'))(\"|\'))+', r"'", step6)
    step6 = re.sub(r'((\")(?=(\")))+', r"'", step6)
    
    for single_quote in step6:
      match_quote = re.match(r'(?<!(\"|\'))(\"|\')', step6)
      step7 = re.sub(r'match_quote{}', r'"', match_quote)
    print(f'{step7}')
    return step7
    
# Path to the original folder
original_folder_path = "/Users/bradleykoch/Library/Mobile Documents/com~apple~CloudDocs/Copywriting/Write-With-AI"

# Base name for the new folder
new_folder_base = "/Users/bradleykoch/Library/Mobile Documents/com~apple~CloudDocs/Copywriting/Write-With-AI-"

# Check if folder exists and increment name if needed
for i in range(1, 1000):  # Assuming you won't have more than 1000 folders with similar names
    new_folder_path = f"{new_folder_base}{i}"
    if not os.path.exists(new_folder_path):
        break
else:
    print("Reached the upper limit of folder names.")
    exit(1)

# Create a copy of the original folder
shutil.copytree(original_folder_path, new_folder_path)

# Get the list of all files in the new directory
file_list = os.listdir(new_folder_path)

# Loop through each file and rename it
for old_filename in file_list:
    new_filename = transform_filename(old_filename)
    old_filepath = os.path.join(new_folder_path, old_filename)
    new_filepath = os.path.join(new_folder_path, new_filename)
    
    # Rename the file
    os.rename(old_filepath, new_filepath)
    print(f'Renamed: {old_filename} -> {new_filename}')