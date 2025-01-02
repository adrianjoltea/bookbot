def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    dic = count_characters(text)
    # print(dic)
    print(print_report(char_sorted_list(dic)))
    # print(f"{num_words} words found in the document")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    lower_text = text.lower()
    char_count = {}
    for char in lower_text:
        if char in char_count:
            char_count[char] += 1
        else :
            char_count[char] = 1
    return char_count

def print_report(char_dict_sorted):
    for item in char_dict_sorted:
        if item['char'].isalpha():
            print(f"The {item['char']} character was found {item['num']} times")

def sort_on(d):
    return d["num"]

def char_sorted_list(char_dict):
    sorted_list = []
    for ch in char_dict:
        sorted_list.append({"char":ch, "num":char_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    

main()
