from stats import words_count
from stats import symbol_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    print(f"{words_count(book_text)} words found in the document")
    print(symbol_count(book_text))

main()