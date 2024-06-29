import mmap

def memory_map_file(file_path):
    with open(file_path, 'r+b') as f:
        
        mmapped_file = mmap.mmap(f.fileno(), 0)
        print(mmapped_file[1:100])

        mmapped_file.close()

memory_map_file('files/destination.bin')