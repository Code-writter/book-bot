
from collections import Counter
import re


def get_book_words(path, regx):
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


#============================================================================

def character_counts_in_file():

    fileUser = "../sample/sample.txt"
    alphabet = "abcdefghijklmnoprstuvyz"

    # // Creating a dictionary #
    countAlp = {}

    for letter in alphabet:
        countAlp[letter] = 0

    # // Reading the file #
    for line in open(fileUser, "r", re.IGNORECASE):
        for letters in line:
            if letters in countAlp.keys():
                countAlp[letters] =  countAlp[letters] + 1

    # // Printing the output #
    print("\n>> In the file, there are;\n")
    for key, value in countAlp.items():
        print(f"{value} times \"{key}\"")



def number_of_words(file_content):
    return len(file_content)

