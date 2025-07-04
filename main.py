from stats import words_count
from stats import symbol_count
from stats import sort_on
from stats import symbol_sorted_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    stats = symbol_count(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {words_count(book_text)} total words")
    print("--------- Character Count -------")
    for symbol in symbol_sorted_list(stats):
        if symbol["char"].isalpha():
            print(f"{symbol["char"]}: {symbol["num"]}")
        else:
            pass
    print("============= END ===============")


main()