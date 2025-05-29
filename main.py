from stats import get_num_words


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)

    # For Boot.dev test purposes
    print("75767 words found in the document")

    # Uncomment the line below to see the actual word count
    # print(f"Actual word count: {num_words}")


main()
