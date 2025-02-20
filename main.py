
def main():
    with open("books/frankenstein.txt") as file:
        file_contents = file.read()
        num_words = count_words(file_contents)
        num_char = char_count(file_contents)

        print(f"--- Begin report of books/frankenstein.txt ---\n{num_words} words found in the document")
        print()
        for letter, count in num_char.items():
            if letter.isalpha():
                print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")


def count_words(s):
    text = s.split()
    return len(text)


def char_count(s):
    counter = {}
    for char in s.lower():
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    return counter



if __name__ == "__main__":
    main()
