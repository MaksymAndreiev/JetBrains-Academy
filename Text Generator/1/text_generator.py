import re

file_name = input()
f = open(file_name, "r", encoding="utf-8")
corpus = f.read()
tokens = re.split(r'[\s]', corpus)[:-1]
print("""Corpus statistics
All tokens: {}
Unique tokens: {}""".format(len(tokens), len(set(tokens))))
idx = input()
while idx != "exit":
    try:
        idx = int(idx)
        try:
            print(tokens[idx])
        except IndexError:
            print("Index Error. Please input an integer that is in the range of the corpus.")
    except ValueError:
        print("Type Error. Please input an integer.")

    idx = input()
