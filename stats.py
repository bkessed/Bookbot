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

def sort_on(symbols):
    return symbols["num"]

def symbol_sorted_list(symbols):
    sorted_list = []
    for symbol in symbols:
        sorted_list.append({"char": symbol, "num": symbols[symbol]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list 

