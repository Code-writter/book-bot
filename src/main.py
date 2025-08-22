path = "../sample/sample.txt"
def get_book_text(path):
    print("Fn called")
    with open (path, 'r') as file:
        print("GEtting ")
        file_content = file.read()
        print(file_content)
        file.close()




get_book_text(path)