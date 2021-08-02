#### Savin Ilya Python Homework №10

input_string = input("Enter number: ")
kollatz_nmb = int(input_string)
counter = 0

while kollatz_nmb != 1:
    counter += 1
    if kollatz_nmb % 2 == 0:
        kollatz_nmb = int(kollatz_nmb / 2)
    else:
        kollatz_nmb = 3*kollatz_nmb + 1

print(counter)