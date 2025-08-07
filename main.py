
def get_book_text(path_to_file):
    with open(path_to_file) as f: 
        book_text = f.read()
        return book_text.split()

def main():
    path_to_file = "books/frankenstein.txt"
    print(f"{len(get_book_text(path_to_file))} words found in the document")

if __name__ == "__main__":
    main()
