def main():
    book_path = "github.com/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    words = read_words(text)
    letters = read_letters(words)
    sortDictionary = sort_dict(letters)
    getReport = get_report(sortDictionary)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def read_words(text):
    words = []
    words = text.split()
    return words

def read_letters(words):
    letters_string = str(words).lower()
    letters_dict = {}
    for char in letters_string:
        if char in letters_dict:
            letters_dict[char] += 1
        else:
            letters_dict[char] = 1
    return letters_dict
    
def sort_dict(letters_dict):
    letters_dict_tuple = list(letters_dict.items())
    letters_dict_tuple.sort(reverse=True, key=get_count)
    return letters_dict_tuple
    
def get_count(i):
    return i[1] 

def get_report(letters_dict_tuple):
    for i in letters_dict_tuple:
        print(f"for the letter {i[0]}, there are {i[1]} occurences ")

main()