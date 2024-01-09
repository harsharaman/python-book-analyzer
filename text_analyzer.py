from src.utils import read_file
from src.word_count_calculations import get_number_of_total_words, get_number_of_unique_words

def main():
    text = read_file()

    words = text.split()
    
    number_of_words = get_number_of_total_words(words)
    number_of_unique_words = get_number_of_unique_words(words)
    
    
    print(f"Total number of words: {number_of_words}")
    print(f"Total number of unique words: {number_of_unique_words}")

if __name__ == '__main__':
    main()