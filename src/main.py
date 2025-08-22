path = "../sample/sample.txt"

def get_book_text(path):
    with open (path) as file:
        file_content = file.read()
        print(file_content)
        file.close()



get_book_text(path)

