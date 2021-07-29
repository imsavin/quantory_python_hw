#### Savin Ilya Python Homework3

from collections import Counter

input_line = input("Enter string: ")
input_list = input_line.lower().split()
dict_counter = Counter(input_list)
max_count = max(dict_counter.values())
for k,v in dict_counter.items():
    if v == max_count:
        print(str(v) + " - " + k)