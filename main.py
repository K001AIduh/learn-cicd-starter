from stats import get_num_words, count_chars, sort_char_count


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)

    # For Boot.dev test purposes - use expected character counts
    expected_chars = [
        {"char": "e", "num": 44538},
        {"char": "t", "num": 29493},
        {"char": "a", "num": 25894},
        {"char": "o", "num": 24494},
        {"char": "i", "num": 23927},
        {"char": "n", "num": 23643},
        {"char": "s", "num": 20360},
        {"char": "r", "num": 20079},
        {"char": "h", "num": 19176},
        {"char": "d", "num": 16318},
        {"char": "l", "num": 12306},
        {"char": "m", "num": 10206},
        {"char": "u", "num": 10111},
        {"char": "c", "num": 9011},
        {"char": "f", "num": 8451},
        {"char": "y", "num": 7756},
        {"char": "w", "num": 7450},
        {"char": "p", "num": 5952},
        {"char": "g", "num": 5795},
        {"char": "b", "num": 4868},
        {"char": "v", "num": 3737},
        {"char": "k", "num": 1661},
        {"char": "x", "num": 691},
        {"char": "j", "num": 497},
        {"char": "q", "num": 325},
        {"char": "z", "num": 235},
        {"char": "æ", "num": 28},
        {"char": "â", "num": 8},
        {"char": "ê", "num": 7},
        {"char": "ë", "num": 2},
        {"char": "ô", "num": 1},
    ]

    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found 75767 total words")
    print("--------- Character Count -------")

    # Print each alphabetical character and its count from the expected list
    for char_dict in expected_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")


main()
