from collections import Counter
from stats import number_of_words
import re


def get_book_text(path, regx):
    with open (path) as file:
        file_content = file.read().lower()

        words = re.findall(regx, file_content )

        word_counts = Counter(words)

        return word_counts




def main():
    path = "../sample/sample.txt"
    regx= r'\b\w+\b'

    word_frequency = get_book_text(path, regx)

    if word_frequency:
        for word, count in word_frequency.items():
            print(f"{word} : {count} ")


main()