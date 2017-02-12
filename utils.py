def read_file(file_path):
    file_handler = open(file_path, 'r')
    return file_handler.readline()