import sys
import os


if len(sys.argv) > 1:
    book_path = sys.argv[1]
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def word_count(text):

    word_num = len(text.split())

    return word_num


def distinct_dict():

    distinct_content = {}

    with open(book_path, encoding='utf-8') as f:
       content = f.read().lower()
       for word in content:
            if word in distinct_content:
               distinct_content[word] += 1
            else:
               distinct_content[word] = 1

    return distinct_content


def text_key_set():

    dict_list = []
    result = distinct_dict()
    
    for key,value in result.items():
        if key.isalpha():
            dict_conversion = {"char": key, "num": value}
            dict_list.append(dict_conversion)
    
    dict_list.sort(key=lambda d: d["num"], reverse=True)

    print(dict_list)
    return dict_list

text_key_set()



