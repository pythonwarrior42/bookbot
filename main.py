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
    return len(words)

def read_letters(words):
    letters_string = str(words).lower()
    letters_dict = {}
    for char in letters_string:
        if char not in letters_dict:
            letters_dict[char] = 0
            letters_dict[char] += 1
    for key, value in letters_dict.items():
     print (key, value   )


main()