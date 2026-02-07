import sys

from stats import count_words, count_characters, sort_report, sort_report

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    frank = sys.argv[1]
    frank_string = get_book_text(frank)
    number_of_words = count_words(frank_string)
    number_of_character = count_characters(frank_string)
    sorted_report = sort_report(number_of_character)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(number_of_words)
    print("--------- Character Count -------")
    for item in sorted_report:
        for key, value in item.items():
            if key.isalpha():
                print(f"{key}: {value}")
    print("============= END ===============")    

if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main()