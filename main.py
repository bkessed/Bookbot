def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    print(f"{words_count(book_text)} words found in the document")

def words_count(book_text):
    return len(book_text.split())

main()