from stats import words_count
from stats import symbol_count
from stats import sort_on
from stats import symbol_sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    stats = symbol_count(book_text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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