from stats import get_book_text


def main():
    path = "../sample/sample.txt"
    regx= r'\b\w+\b'

    word_frequency = get_book_text(path, regx)

    if word_frequency:
        for word, count in word_frequency.items():
            print(f"{word} : {count} ")


main()