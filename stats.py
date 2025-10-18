def count_words(text):
    words = text.split()
    return len(words)

def  count_characters(text):
    counted_letters ={}
    letters = list(text)
    for letter in letters:
        letter = letter.lower()
        if letter in counted_letters:
            #print(letter)
            counted_letters[letter] += 1
        else:
            #print(letter)
            counted_letters[letter] = 1
    return counted_letters

def sort_on(counted_letters):
    return dict(sorted(counted_letters.items(), key=lambda item: item[1], reverse=True))

def sort_on_helper(dict_item):
    return dict_item["num"]

def chars_dict_to_sorted_list(char_count_dict):
    # Convert dictionary to list of dictionaries
    char_list = []
    for char, count in char_count_dict.items():
        char_list.append({"char": char, "num": count})
    
    # Sort the list from greatest to least by count
    char_list.sort(key=sort_on_helper, reverse=True)
    
    return char_list