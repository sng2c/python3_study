import os

with open("test.txt") as file_handle:
    with open("test2.txt",mode="w") as file_out:
        for idx, line in enumerate(file_handle):
            line2 = line.rstrip()
            user = line2.split(",")
            if user[0] == "cdkdkdk":
                print(user[0]+",5555")
            else:
                print(line2)




# os.rename("test.txt", "test.txt.bak")
# os.rename("test2.txt", "test.txt")
#
