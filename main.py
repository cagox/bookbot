def open_book(filename):
    file_contents = ""
    with open(filename) as f:
        file_contents += f.read()
        return file_contents

def word_count(file_contents):
    words = file_contents.split()
    return len(words)

def character_counts(text):
    chars = {}
    text = text.lower()
    for c in text:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def sorted_characters(char_dict):
    new_dict = {}
    for k in char_dict:
        if k.isalpha():
            new_dict[k] = char_dict[k]
    tuples = list(new_dict.items())
    tuples.sort(key=lambda tup: tup[1], reverse=True)
    return dict(tuples)





def main():
    book = open_book('books/frankenstein.txt')
    character_dict = character_counts(book)
    sorted_chars = sorted_characters(character_dict)
    print(word_count(book), "words found in the document\n")
    for c in sorted_chars:
        print(f"The '{c}' character was found {sorted_chars[c]} times")
    print("--- End report ---")





main()