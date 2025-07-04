def words_count(book_text):
    return len(book_text.split())

def symbol_count(book_text):
    stats = {}
    for symbol in book_text.lower():
        if symbol in stats:
            stats[symbol] += 1
        else:
            stats[symbol] = 1
    return stats