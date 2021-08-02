#!/usr/bin/python3
# Savin Ilya Python Homework N2

input_line = input("Enter string: ")
input_list = input_line.split()
output_dict = {}
for i in input_list:
    output_dict[i] = i
for i in output_dict:
    print((output_dict[i]), end=" ")
