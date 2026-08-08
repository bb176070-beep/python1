

# hai = ["hallo","car","bike",12536,"kjahs","bike"]

#append
# hai.append("brazil")
# print("\n","append =",hai)   #item will add on last position
#
# #remove
# hai.remove("brazil")
# print("\n","remove =",hai)

# #count
# print("\n","count =",hai.count("bike"))

# #index
# print("\n","index =",hai.index("car",))

#copy
# hallo = hai.copy()
# hallo.append("messi")
# print("\n","copy =",hallo)    #using copy items other files in list are not allowed
#
# #insert
# hai.insert(2,"messi")
# print("\n","insert =",hai)
#
# #clear
# hai.clear()
# print("\n","clear =",hai)
#
# #pop
# hallo = ["apple", "banana", "cherry"]
# hallo.pop(0)        #last item only remove
# print("\n","pop =",hallo)

#delete
# x=[12,3,4,5,55]
# del x
# print(x)


# a=[12,3,4,5,6]
# a.sort(reverse=True)
# print(a)

#
# c=["zam","abc","fgh","bcd"]
# c.sort(reverse=True)
# print(c)


# a=["Zbc","abc","zam","Bcd"]
# a.sort(key=str.lower)
# print(a)



# a=[12,3,3,3]
# b=["hello","Kk"]
# a.extend(b)
# print(a)



# list()


# a=(12,3,3,4,4,4)
# print(type(a))
# b=list(a)
# print(b)

# lisy = ((1,2,4,56,5))
# print(lisy)


a = int(input("enter the number:"))
b = int(input("enter the number:"))
c = int(input("enter the number:"))

z = a,b,c

list(z)