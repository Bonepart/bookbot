def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt")
        print(f"{process_text(file_contents)} words found in the document")
        print("")
        char_dict = count_characters(file_contents)
        char_list = list(char_dict.items())
        char_list.sort()
        for item in char_list:
            print(f"The {item[0]} character was found {item[1]} times")
        

def process_text(book):
    words = book.split()
    return len(words)

def count_characters(book):
    book = book.lower()
    data = {}
    for char in book:
        if char.isalpha():
            if char not in data:
                data[char] = 1
            else:
                data[char] += 1
    return data

main()