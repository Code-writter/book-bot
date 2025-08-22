from stats import number_of_words


def get_book_text(path):
    with open (path) as file:
        file_content = file.read()
        word_counts = number_of_words(file_content)
        print(word_counts)
        file.close()




def main():
    path = "../sample/sample.txt"
    print(path)
    get_book_text(path)


main()