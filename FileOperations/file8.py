def copy_binary_file(source, destination):
    with open(source, 'rb') as src_file:
        with open(destination, 'wb') as dest_file:
            while True:
                chunk = src_file.read(1024)
                if not chunk:
                    break

                dest_file.write(chunk)

copy_binary_file('files/source.bin', 'files/destination.bin')