def get_word_count(path_to_file):
    with open(path_to_file) as f: 
        book_text = f.read()
        return len(book_text.split())

def character_count(path_to_file):
    character_dict = {}
    with open(path_to_file) as f:
        book_text = f.read()
        lowercase_book_text = book_text.lower()
        character_list = list(lowercase_book_text)
        for c in character_list:
            if c in character_dict:
                character_dict[c] += 1
            else:
                character_dict[c] = 1
    return character_dict