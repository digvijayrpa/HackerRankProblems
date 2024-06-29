import os

def merge_files(output_file, *input_files):
    with open(output_file, 'w') as outfile:
        for fname in input_files:
            with open(fname, 'r') as infile:
                for line in infile:
                    outfile.write(line)

merge_files('files/file4.txt', 'files/file4_1.txt', 'files/file4_2.txt')