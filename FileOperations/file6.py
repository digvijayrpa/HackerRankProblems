def process_large_files(files_path, chunk_size=1024):
    with open(files_path, 'r') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            
            process_chunk(chunk)

def process_chunk(chunk):
    words = chunk.split()
    word_count = len(words)
    print(f"Processed chunk with {word_count} words")


process_large_files('files/file3.txt')