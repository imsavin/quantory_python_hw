#!/usr/bin/python3
# Savin Ilya Python Homework N8

def recursive_func():
    input_str = input("Enter number: ")
    if input_str == "cancel":
        print("Bye!")
    else:
        try:
            if (int(input_str) % 2) == 0:
                print (int(int(input_str)/2))
            else:
                print(int(input_str)*3 + 1)
        except ValueError:
            print("Can't convert entered text to number")
        recursive_func()


recursive_func()
