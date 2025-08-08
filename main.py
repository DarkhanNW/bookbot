from stats import get_word_count, character_count
def main():
    path_to_file = "books/frankenstein.txt"
    print(f"{(get_word_count(path_to_file))} words found in the document")
    print(character_count(path_to_file))

if __name__ == "__main__":
    main()
 