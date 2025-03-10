from typing import DefaultDict, Dict
from collections import defaultdict


def get_num_words(book_text: str) -> int:
    num_words = len(book_text.split())
    return num_words


def get_char_count(book_text: str) -> DefaultDict[str, int]:
    chars: DefaultDict[str, int] = defaultdict(int)
    for char in book_text.lower():
        chars[char] += 1
    return chars


def get_char_count_list(chars: DefaultDict[str, int]) -> Dict[str, int]:
    new_chars = {char: count for char,
                 count in chars.items() if char.isalpha()}
    chars = sorted(new_chars.items(), key=lambda item: item[1], reverse=True)
    return list(chars)
