def main():
    book_path = "github.com/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    words = read_words(text)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def read_words(text):
    words = []
    words = text.split()
    return words

main()