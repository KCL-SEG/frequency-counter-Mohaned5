"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


from collections import Counter


def frequencies(items):
    frequencies = {}
    string_list = [str(item) for item in items]
    count_items = Counter(string_list)
    for key in count_items.keys():
        print(str(key) + ":" + str(count_items[key]))
        frequencies[key] = count_items[key]
    return frequencies
