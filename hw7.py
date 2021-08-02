#### Savin Ilya Python Homework №7

pw_file=open("/etc/passwd",'r')
gr_file=open("/etc/group",'r')
shells_dict = {}
users_dict  = {}
pw_list = []
for line in pw_file:
    pw_list = line.split(":")
    shells_dict[pw_list[-1].strip("\n")] = shells_dict.get(pw_list[-1].strip("\n"),0) + 1
    users_dict[pw_list[0].strip("\n")] = pw_list[2].strip("\n")
    
print(shells_dict)

pw_file.close()
tmp_line=""

for line in gr_file:
    tmp_line = line.split(":")[0] + ": "
    for users in line.split(":")[3].split(","):
        if len(users.strip("\n")) > 0:
               tmp_line += users_dict[users.strip("\n")] + ","
    print(tmp_line)

gr_file.close()