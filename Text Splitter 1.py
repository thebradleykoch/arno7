import os
import re


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
