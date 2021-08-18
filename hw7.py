#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Savin Ilya Python Homework N7

# ---------
# Напишите программу, которая читает данные из файлов
# /etc/passwd и /etc/group на вашей системе и выводит
# следующую информацию в файл output.txt:
# 1. Количество пользователей, использующих все имеющиеся
# интерпретаторы-оболочки.
# ( /bin/bash - 8 ; /bin/false - 11 ; ... )
# 2. Для всех групп в системе - UIDы пользователей
# состоящих в этих группах.
# ( root:1, sudo:1001,1002,1003, ...)
# ----------

pw_file = open("passwd", 'r')
gr_file = open("group", 'r')
shells_dict = {}
users_dict = {}
pw_list = []
for line in pw_file:
    pw_list = line.split(":")
    shells_dict[pw_list[-1].strip()
                ] = shells_dict.get(pw_list[-1].strip(), 0) + 1
    users_dict[pw_list[0].strip()] = pw_list[2].strip()

print(shells_dict)
print()

pw_file.close()
tmp_line = ""

for line in gr_file:
    tmp_line = line.split(":")[0] + ": "
    for users in line.split(":")[3].split(","):
        if len(users.strip()) > 0:
            tmp_line += users_dict[users.strip()] + ","
    print(tmp_line)

gr_file.close()
