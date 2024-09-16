import openai
import os
import re


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


# Decide whether to split the file or not
split = False

# Execute the split_file function
if split == True:
    split_file(
        '/Users/bradleykoch/Downloads/How to Make Your First $1000 With ChatGPT (still early) - cleaned_v1.txt', 10000)


# --------------------------------------------


# Select input file
input_file = "/Users/bradleykoch/Downloads/How to Make Your First $1000 With ChatGPT (still early) - cleaned_v1_chunk_1.txt"

# Name the output file
output_file = "/Users/bradleykoch/Downloads/How to Make Your First $1000 With ChatGPT (still early) - cleaned_v1_chunk_1_OpenAI_Summary.txt"

# Set up the user prompt (instructions or context for the example text)
user_prompt_0 = "Summarize the following YouTube video transcript, focusing on actionable ideas, insights, and takeaways. Include chapter headings and subheadings where appropriate. Use bullet points or numbered lists that are easy to scan. These lists can be full sentences or short phrases. Include a section at the end with the speaker's most convincing opinions, what he sounds most excited about, and where he sees the greatest potential opportunities for the near future. Your summary should be 1-2 pages long."


summary_part_a = "/Users/bradleykoch/Downloads/How to Make Your First $1000 With ChatGPT (still early) - cleaned_v1_chunk_0_OpenAI_Summary.txt"

summary_part_b = "/Users/bradleykoch/Downloads/How to Make Your First $1000 With ChatGPT (still early) - cleaned_v1_chunk_1_OpenAI_Summary.txt"

new_total_summary = "/Users/bradleykoch/Downloads/How to Make Your First $1000 With ChatGPT (still early) - cleaned_v1_OpenAI_Total_Summary.txt"

# Merge the separate output files into one file to create one total summary
# Read the contents of the two input files
with open(summary_part_a, 'r') as part_a:
    summary_part_a_content = part_a.read()

with open(summary_part_b, 'r') as part_b:
    summary_part_b_content = part_b.read()

# Concatenate the contents with headers
summary_input_file = "Summary Part 1\n\n\n" + summary_part_a_content + \
    "\n\n\n\nSummary Part 2\n\n\n" + summary_part_b_content

# Write the concatenated contents to a new file
with open(new_total_summary, 'w') as f:
    f.write(summary_input_file)


# Name the output file
summary_output_file = "/Users/bradleykoch/Downloads/How to Make Your First $1000 With ChatGPT (still early) - cleaned_v1_OpenAI_Full_Summary.txt"


user_prompt_summary = "The following is a summary of the YouTube video transcript, divided into two consecutive parts. Create a merged summary that effectively combines the content of 'Summary Part 1' and 'Summary Part 2'. Keep the headers and subheaders the same. You may rephrase content slightly for clarity and conciseness, but err on the side of keeping the original content intact. Your summary should be roughly 3/4 the length of Summary Parts 1 and 2 combined together."


'''
# Read the input file
with open(input_file, "r") as file:
    file_prompt = file.read()
    '''
with open(new_total_summary, 'r') as file_summary:
    file_summary = file_summary.read()

# Join the user prompt and the file prompt
joined_prompt = user_prompt_summary + \
    "\n\n***\n\n" + file_summary + "\n\n***\n\n"

# Set up the API key
openai.api_key = "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"

# Generate response
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=joined_prompt,
    max_tokens=800,
    n=1,
    stop=None,
    temperature=0.7,
)

# Get the generated text
generated_text = response["choices"][0]["text"]

# Save the generated text to a file
with open(summary_output_file, 'w') as f:
    f.write(generated_text)
    print("Full Summary saved successfully.")
