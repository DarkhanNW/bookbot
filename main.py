import sys
from stats import open_utf8, get_word_count, character_count

def main():
    if len(sys.argv) != 2:
        raise Exception("Usage: python3 main.py <path_to_book>")
        return
    path_to_file = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {(get_word_count(path_to_file))} total words")
    print("--------- Character Count -------")
    sorted_characters = character_count(path_to_file)
    for sc in sorted_characters:
        sorted_char = sorted_characters[sc]
        print(f"{sc}: {sorted_char}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
 