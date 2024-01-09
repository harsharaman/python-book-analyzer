import argparse

def read_file():
    parser = argparse.ArgumentParser()

    parser.add_argument('--file_path', help="Path to the input text (.txt) file.")

    args = parser.parse_args()

    with open(args.file_path, 'r') as file:
        contents = file.read()
    
    return contents