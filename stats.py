def open_utf8(filename, mode='r'):
    return open(filename, mode, encoding="utf-8")

def get_word_count(path_to_file):
    with open_utf8(path_to_file) as f: 
        book_text = f.read()
        return len(book_text.split())

def character_count(path_to_file):
    character_dict = {}
    with open_utf8(path_to_file) as f:
        book_text = f.read()
        lowercase_book_text = book_text.lower()
        character_list = list(lowercase_book_text)
        for c in character_list:
            if c in character_dict:
                character_dict[c] += 1
            elif c.isalpha() == True:
                character_dict[c] = 1
    sorted_characters = dict(sorted(character_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_characters
