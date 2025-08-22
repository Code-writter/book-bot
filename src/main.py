path = "../sample/sample.txt"

def get_book_text(path):
    with open (path) as file:
        file_content = file.read()
        word_counts = number_of_words(file_content)
        print(word_counts)
        file.close()




def number_of_words(file_content):
    return len(file_content)



get_book_text(path)

