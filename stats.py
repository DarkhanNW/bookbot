def get_word_count(path_to_file):
    with open(path_to_file) as f: 
        book_text = f.read()
        return len(book_text.split())