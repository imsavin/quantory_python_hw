#!/usr/bin/python3
# Savin Ilya Python Homework N6

def ispalindromic(s):
    reversed_string = s[::-1]
    return s == reversed_string


summ = 0
for i in range(1, 1000000):
    if ispalindromic(str(i)) and ispalindromic("{0:b}".format(i)):
        summ += i

print(summ)
