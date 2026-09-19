# a = open("hallo.txt","w")


# f = open("hallo.txt","r")
# print(f.read())

# print(f.readline())
# print(f.readline())

# g = open("jhg.txt","a")
# g.write("hallodfff")


# name = input("Enter your name: ")
# age = input("Enter your age: ")
#
# with open("file.txt", "a") as file:
#     file.write(name + ", " + age + "\n")
#
# print("ok")
#
# with open("file.txt", "r") as file:
#     data = file.read()
#     print(data)


name = input("Enter your name: ")
new_age = input("Enter your age: ")

with open("file.txt", "r") as file:
    taken = file.readlines()

with open("file.txt", "w") as file:
    for take in taken:
        data = take.strip().split(",")

        if data[0] == name:
            file.write(name + ","+new_age + "\n")
        else:
            file.write(take)
print("ok")
