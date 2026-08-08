# def name():
#
#     print("Hello World")
#
#
# name()
# dry
from fontTools.misc.cython import returns


# arg and para

# def name(a):
#     print(a)
#
#
#
#
# name(23)
#
# def name():
#     a=18
# #if and else
#
# a = int(input("enter the number :"))
# b = int(input("enter the number :"))
# def hai():
#     if a > b :
#         print("a is greater than b")
#     else:
#         print("b is greater than a")
# hai()
#
#
# #for loop
# a = [23,4,5,6,8]
# def hallo():
#     for i in a:
#         print(i)
# hallo()
#
# #while loop
# b = int(input("enter a number: "))
# def hadhi():
#     a = b
#     while a <=100:
#         print(a)
#         a += 1
#
# hadhi()

#1)write a function to find largest digit in a number
#2)second largest digit in a number using function
#3)print patern using function
# 1
#22
#333
#4444
#55555


#1)write a function to find largest digit in a number
#
# a = int(input("enter the number:"))
# def hallo(a):
#     large = 0
#     while a > 0:
#         c = a % 10
#         if c > large:
#             large = c
#         a = a // 10
#     print("it is largest",large)
# hallo(a)

#2)second largest digit in a number using function
# def second_largest(n):
#     large = -1
#     scd_large = -1
#     while n > 0:
#         digit = n % 10
#         if digit > large:
#             scd_large = large
#             large = digit
#         elif digit > scd_large and digit != large:
#             scd_large = digit
#         n = n // 10
#     print("Second largest digit:", scd_large)
# a = int(input("Enter a number: "))
# second_largest(a)


#3)print patern using function
# 1
#22
#333
#4444
#55555
#
# def pattern(n):
#     for i in range(n):
#         for j in range(i):
#             print(i, end=" ")
#         print()
# a = int(input("enter the number :-"))
# pattern(a)

# def hello(*x):
#     print(x[6])
#
#
#
# hello(12,3,4,4,5,5,50,5,6,6,6,6,7)

# def hai(*args):
#     print(args[4])
#
#
# hai(3,68,94,60,29,48)


# def keyw(name,age,place):
#     print(name)
#     print(age)
#     print(place)
#
#
#
#
# keyw(name="hadi",age=12,place="pmna")
#
# def keyword(name,place,number):
#     print(name)
#     print(place)
#     print(number)
#
# keyword(name="roi",place="goa",number=1)




# def defa(name="azaman"):
#     print(name)
#
#
#
# defa("hello")
# defa(12)
# defa("hello1")
# defa()

# def default(name="palace"):
#     print(name)
#
# default("kshd")
# default(7)
# default("hadi")
# default()

# def keyword_arg(**arg):
#     print(arg)
#
#
# keyword_arg(name="hallo",age = 20,place="vdk")

# def keyword_arg(**arg):
#     print(arg["name"])
#
#
# keyword_arg(name="hallo",age = 20,place="vdk")




# def ad(x,y):
#     return x+y
#
# ob=ad(10,20)
# print(ob)

# print(ad(10,20))

# def hallo(a):
#     b =0
#     while a > 0:
#         c = a % 10
#         b = b * 10 + c
#         a = a // 10
#     return b
# x = int(input("enter number :"))
# print(hallo(x))

# def hallo(a):
#     b =0
#
    # while a > 0:
    #     c = a % 10
    #     b = b * 10 + c
    #     a = a // 10
#     return b
# x = int(input("enter number :"))
# f = hallo(x)
# if x==f:
#     print("it is palindrome")
#
# else:
#     print("it is not palindrom")

# def hai(a):
#     b = 0
#     while a > 0:
#         b = b * 10 + a % 10
#         a = a // 10
#     return b
# x = int(input("Enter a number: "))
# f = hai(x)
# if True:
#     if x == f:
#         print("it is palindrome")
#     else:
#         print("it is not palindrome")



# x=34
# y=67
# def glob():
#     a=12   #LOCAL
#     b=30
#     print(a+b)
#     print(x+y)
#
# glob()
#
# print(x+y)
# print(a+b)

# a = 19
# def gobal():
#     print(a)
# gobal()
# print(a)
# def local():
#     a = 23
#     print(a)
# local()






