def main():
    book_path = "github.com/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    

