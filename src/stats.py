
from collections import Counter
import re


def get_book_text(path, regx):
    try:
        with open (path, 'r', encoding="utf-8") as file:
            file_content = file.read().lower()

            # Use regex to find all words (alphanumeric sequences)
            words = re.findall(regx, file_content )

            word_counts = Counter(words)

            return word_counts
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return {}



def number_of_words(file_content):
    return len(file_content)

