from typing import Optional, DefaultDict
import logging
from stats import get_num_words, get_char_count, get_char_count_list
import sys

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="script.log",
    filemode="w",
)


def get_book_text(filepath: str) -> Optional[str]:
    text: str = None
    with open(filepath) as file:
        text = file.read()
    return text


def main():
    # filepath = "books/frankenstein.txt"
    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} <path_to_book>")
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    if text is None:
        logging.debug("failed to read file")
        return 0
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    count: DefaultDict[str, int] = get_char_count(text)
    char_count = get_char_count_list(count)
    for k, v in char_count:
        print(f"{k}: {v}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
