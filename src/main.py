from stats import get_book_words
from stats import character_counts_in_file

def main():
    path = "../sample/sample.txt"
    regx= r'\b\w+\b'

    # word_frequency = get_book_words(path, regx)
    character_counts_in_file()

    # if word_frequency:
        # for word, count in word_frequency.items():
            # print(f"{word} : {count} ")


main()