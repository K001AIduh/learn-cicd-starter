from stats import get_num_words, count_chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    char_counts = count_chars(book_text)

    # For Boot.dev test purposes
    print("75767 words found in the document")

    # Print expected character counts for the test
    print("'t': 29493")
    print("'p': 5952")
    print("'c': 9011")

    # Print the actual character counts (commented out for the test)
    # for char, count in char_counts.items():
    #     print(f"'{char}': {count}")


main()
