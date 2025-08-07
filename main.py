
def get_book_text(path_to_file):
    with open(path_to_file) as f: 
        return f.read()

def main():
    path_to_file = "books/frankenstein.txt"
    print(get_book_text(path_to_file))

if __name__ == "__main__":
    main()
