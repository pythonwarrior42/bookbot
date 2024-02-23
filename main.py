def main(): #main function which calls all functions in order
    book_path = "github.com/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    words = read_words(text)
    letters = read_letters(words)
    sortDictionary = sort_dict(letters)
    getReport = get_report(sortDictionary)

def get_book_text(path):        # opens the file 
    with open(path) as f:
        return f.read()
    
def read_words(text):       #reads the text in the file using the output from get_book_text function and moves it into a lsit
    words = []
    words = text.split()
    return words

def read_letters(words):                        #splits the words list into a string of letters
    letters_string = str(words).lower()
    
    letters_dict = {}                           #
    for char in letters_string:                 #This sorts the letters in the string into a dictionary, if the letter is seen, it is incremented by 1, if not, it is assigned the value 1. 
        if char in letters_dict:                # It does this by iterating over the string using a for loop
            letters_dict[char] += 1
        else:
            letters_dict[char] = 1
    return letters_dict
    
def sort_dict(letters_dict):                                #this function sorts the letters dictionary, by moving it into a tuple.
    letters_dict_tuple = list(letters_dict.items())
    letters_dict_tuple.sort(reverse=True, key=get_count)
    return letters_dict_tuple
    
def get_count(i):           #gets count of occurence of the letters so it can be used as the key to sort
    return i[1] 

def get_report(letters_dict_tuple):             # returns the report, of the letters and their occurences, removing punctuation
     for i in letters_dict_tuple:
        if i[0].isalpha():
          print(f"for the letter {i[0]}, there are {i[1]} occurences ")

main()