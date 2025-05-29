def get_num_words(text):
    words = text.split()
    return len(words)


def count_chars(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts


def sort_char_count(char_counts):
    # Create a list to store dictionaries of characters and their counts
    sorted_chars = []

    # Convert the character count dictionary to a list of dictionaries
    for char, count in char_counts.items():
        sorted_chars.append({"char": char, "num": count})

    # Sort the list by count (num) in descending order
    def sort_on(dict):
        return dict["num"]

    sorted_chars.sort(reverse=True, key=sort_on)

    return sorted_chars
