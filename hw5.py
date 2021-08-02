#### Savin Ilya Python Homework №5

input_string = input("Enter string of numbers: ")
numbers_list = []
split_string = input_string.split()
for i in split_string:
    numbers_list.append(int(i))


numbers_list.sort()
numbers_list = list(set(numbers_list)) #delete duplicates

counter = 0
flag = 0
for i in numbers_list:
    counter += 1
    if i > counter:
        print(counter)
        flag = 1
        break

if flag == 0:
    print(counter+1)

