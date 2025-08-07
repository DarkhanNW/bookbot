from stats import get_word_count

def main():
    path_to_file = "books/frankenstein.txt"
    print(f"{(get_word_count(path_to_file))} words found in the document")

if __name__ == "__main__":
    main()
