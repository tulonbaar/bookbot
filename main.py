import sys
from stats import count_words, count_characters, chars_dict_to_sorted_list

def get_book_text(filepath):
    with open(filepath, "r") as file:
        return file.read()

def main():
    print("============ BOOKBOT ============")
    book_text = get_book_text(filepath)
    if(not book_text):
        print("Error: Could not read book text.")
        return
    else:
        print(f"Analyzing book found at {filepath}")

    # Word count
    print("--------- Word Count -----------")
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_count = count_characters(book_text)
    sorted_chars = chars_dict_to_sorted_list(char_count)
    
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

if(len(sys.argv) == 2):
    filepath = sys.argv[1]
    main()
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
