import re
import requests
from bs4 import BeautifulSoup

url = "https://www.udemy.com/course/ninja-writing-the-four-levels-of-writing-mastery/learn/lecture/4395688#overview"  # replace with your URL
response = requests.get(url)
html_content = response.text # Now you can use html_content with BeautifulSoup

# Use the 'html.parser' to parse the page
# soup = BeautifulSoup(html_content, 'html.parser')

def extract_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract section name
    section_name = soup.find('span', {'class': 'truncate-with-tooltip--ellipsis--2-jEx'}).text.strip()

    # Extract module name
    module_name = soup.find('span', {'data-purpose': 'item-title'}).text.strip()

    # Extract transcript text
    transcript_text = []
    transcript_cues = soup.find_all('span', {'data-purpose': 'cue-text'})
    for cue in transcript_cues:
        transcript_text.append(cue.text.strip())

    return section_name, module_name, transcript_text

# Assuming 'html_content' contains the HTML content
section_name, module_name, transcript_text = extract_content(html_content)

print(f"Section Name: {section_name}")
print(f"Module Name: {module_name}")
print(f"Transcript Text: {transcript_text}")


# 
# module_name = input("Enter module name: ")
# module_transcript_file_name = re.sub(r'\.\w*', r'', module_name, flags=re.I |
#                           re.M) + "-" + input("Enter module transcript file name suffix: ") + ".txt"
# module_transcript_file_name = re.sub(r'\s', r'-', module_transcript_file_name, flags=re.I |
#                           re.M)

# # Make a request to the website
# r = requests.get("https://www.udemy.com/course/ninja-writing-the-four-levels-of-writing-mastery/learn/lecture/4395688#overview")
# r.content

# # Use the 'html.parser' to parse the page
# soup = BeautifulSoup(r.content, 'html.parser')

# # Find the transcript text in the HTML
# # This will depend on the structure of the webpage, but it might look something like this:
# transcript_text = soup.find_all('span', attrs={'data-purpose': 'cue-text'})

# # Extract the text from the transcript
# transcript = [t.text for t in transcript_text]

# # Join all the text together into one string
# full_transcript = ' '.join(transcript)



# # Save the transcript to a text file
# with open(module_transcript_file_name, 'w') as f:
#     f.write(full_transcript)
