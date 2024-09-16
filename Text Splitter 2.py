import os
import re


def str_len(string):
    text_string = re.sub(r'\n', ' ', string)
    print(len(text_string))

# Paste string into function
str_len("""AI Money-Making Ideas

Max’s Introduction
- AI is creating essays, coding, solving math problems, even writing apology letters 
- People will pay for convenience, even if the task can be done for free 
- AI businesses must provide value and convenience 

The Opportunity Paradox
- AI will take our jobs, but also open up doors for new businesses 
- People will pay to solve problems, even if they can solve them themselves 
- Value through convenience is key to making money with AI 

Improving AI Businesses
- User experience is the key to distinguishing AI businesses 
- Brainstorming ideas is the best way to get started 
- Improve AI businesses by offering increased convenience and a great platform 

AI Business Ideas
- Prompt Based.com: Sell AI prompts to others 
- Business Name Generator: Provide a convenient service to generate business names 
- Fitness Coach: Use AI to create a fitness coach service 
- Web Design Concepts: Create a convenient service to design web concepts 

Most Convincing Opinions
Max believes that value through convenience is the key to making money with AI. He suggests brainstorming ideas and improving AI businesses by offering increased convenience and a great platform. He also believes that user experience is the key to distinguishing AI businesses.""")

"""

def file_len(filename):
    with open(filename, 'r') as f:
        full_length = len(f.read())
        '''for i, l in enumerate(f):
            pass
    return i + 1'''


def split_file(filename, chunk_size):
    # Open the file in text mode
    with open(filename, 'r') as file:
        # Calculate the number of chunks
        file_size = os.path.getsize(filename)
        num_chunks = os.path.getsize(filename) // chunk_size
        if os.path.getsize(filename) % chunk_size > 0:
            num_chunks += 1

        ready = True

        # Split the file into chunks
        if ready == True:
            for i in range(num_chunks):
                chunk = file.read(chunk_size)
                # Write the chunk to a new file
                with open(f'{filename}_chunk_{i}.txt', 'w') as chunk_file:
                    chunk_file.write(chunk)
        else:
            with open(filename, 'r') as file:
                full_text = file.read()
                full_length = len(full_text)
                num_chunks = full_length // chunk_size
                if full_length % chunk_size > 0:
                    num_chunks += 1

    print(f"file_size: {file_size}, num_chunks: {num_chunks}.")


# Execute the function
split_file(
    '/Users/bradleykoch/Downloads/How to Make Your First $1000 With ChatGPT (still early) - cleaned_v1.txt', 10000)
"""
