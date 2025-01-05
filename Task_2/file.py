import string
filename = input("Enter the name of the text file: ")
word_count = {}

try:
    with open(filename, 'r') as file:
        text = file.read()
        text = text.translate(str.maketrans('', '', string.punctuation)).lower()
        words = text.split()
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    print("\nWord counts in alphabetical order:")
    for word in sorted(word_count):
        print(f"{word}: {word_count[word]}")

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
