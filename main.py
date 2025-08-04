import sys
from stats import find_word_count
from stats import find_char_count
from stats import my_sorted_dict 

def get_book_text(filepath): 
    with open(filepath) as f: 
        file_contents = f.read()
    return file_contents



def main():
    if sys.argv[-1] == 'main.py':
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    file_contents = get_book_text(filepath)
    file_word_count = find_word_count(file_contents)
    file_char_count = my_sorted_dict(find_char_count(file_contents))

    print(f"============ BOOKBOT ============ \n Analyzing book found at {sys.argv[1]} \n ----------- Word Count ---------- \n")
    print(f"Found {file_word_count} total words")
    print("----------- Character Count -----") 
    
    for item in file_char_count: 
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()


    
    
