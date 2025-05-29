def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    # Create an empty dictionary to store letter counts
    letter_counts = {}
    # Convert text to lowercase to count uppercase and lowercase letters together
    lowered_text = text.lower()

    # Count the frequency of each letter
    for char in lowered_text:
        # Only count letters, not spaces, numbers, or punctuation
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

    return letter_counts


def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    letter_counts = count_letters(book_text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    # Create a list of letters sorted by frequency (highest to lowest)
    chars_sorted_by_frequency = sorted(
        letter_counts.items(), key=lambda item: item[1], reverse=True
    )

    # Print each letter and its count
    print("The most common letters in the text are:")
    for char, count in chars_sorted_by_frequency:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")


main()
