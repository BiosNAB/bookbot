import sys
import os

from stats import word_count
from stats import distinct_dict
from stats import text_key_set

if len(sys.argv) > 1:
    book_path = sys.argv[1]
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    



def get_book_text(book_path):

    with open(book_path, encoding='utf-8') as f:
       content = f.read()
    return content


def main():

    book_text = get_book_text(book_path)
    count = word_count(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for key_set in text_key_set():
        print(f"{key_set['char']}: {key_set['num']}")


main()
